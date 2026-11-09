#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string>
#include <cerrno>
#include <array>
#include <sys/time.h>

/**
 * POSIX-Socket-API basics:
 * 
 * socket():   // erzeugt einen kommunikations endpunkt und gibt den file descriptor zurück.
 * bind():      // verknüpft einen socket mit einer netzwerkadress und portnummer
 * accept():    // nimmt die erste anstehende verbindungsanfrage entgegen und erstellt einen komplett neuen socket pro verbindung.
 * close():     // gibt den socket-descriptor frei und leitet das schließen der eigentlichen netzwerverbindung ein.
 *
 * g++ command:
 * g++ -Wall -Wextra -Wpedantic src/main.cpp -o system-service
 */

 struct HttpRequest {
    std::string method;
    std::string target;
    std::string version;
};

enum class ReadResult {
    Complete,   // Header vollständig gelesen
    TooLarge,   // Header überschreited größenlimit
    Closed,     // Client hat die Verbindung vorzeitig geschlossen
    Timeout,    // Der Empfang hat zu lange auf weitere Daten gewartet
    Error       // Sonstiger Socket-Fehler
};

ReadResult readHttpHeaders (int client_fd, std::string& headers) {
    constexpr size_t MAX_HEADER_SIZE = 8192;   // 8 KiB

    std::array<char, 1024> buffer{};

    headers.clear();

    while (true) {
        ssize_t bytes_recieved = recv(
            client_fd,
            buffer.data(),
            buffer.size(),
            0
        );

        if (bytes_recieved == -1) {
            if (errno == EINTR) {
                continue;
            }

            if (errno == EAGAIN || errno == EWOULDBLOCK) {
                return ReadResult::Timeout;
            }

            return ReadResult::Error;
        }

        if (bytes_recieved == 0) {
            return ReadResult::Closed;
        }

        headers.append(
            buffer.data(),
            static_cast<size_t>(bytes_recieved)
        );

        // Check for end of http headerss
        size_t header_end = headers.find("\r\n\r\n");

        if (header_end != std::string::npos) {
            size_t header_length = header_end + 4;
            
            if (header_length > MAX_HEADER_SIZE) {
                return ReadResult::TooLarge;
            }

            headers.resize(header_length);
            return ReadResult::Complete;
        }

        if (headers.size() > MAX_HEADER_SIZE) {
            return ReadResult::TooLarge;
        }
    }
}

int main() {
    /*
     * fd => File Descriptor
     *
     * socket(AF_INET, SOCK_STREAM, 0);
     * socket(Ipv4-Adressfamilie, Verbindungsorientierter Byte-Stream (hier TCP), Standardprotokoll für diese Kombination verwenden)
     *
     * socket erstellt keinen http server und auch noch keinen TCP-Listener. sondern liefert zunächst eine vom Linux-Kernel verwalteten Socket-Endpunkt erzeugten referenz zurück.
     * das ist die fileDescriptor nummer.
     * diese muss immer positiv sein.
     * 0 => standard input
     * 1 => standard output
     * 2 => standard error
     * 3 => socket => Kernel-Opjekt TCP Socket (daher wird diese descriptor number auf den meisten linux geräten 3 sein)
     * 
     * C++ besitzt dabei nicht den gesammten Socket. Es besitzt legidlich einen descriptor mit dem es den sockel ansprechen kann.
     * Vermutung: Dadurch denke ich können mehere programme einheitliche operationen benutzen. also könnten wir vielleicht den socket auch mit red() und write() ansprechen?
    */

    int server_fd = socket(AF_INET, SOCK_STREAM, 0); // 
    if (server_fd == -1) {
        std::cerr << "Failed to create socket\n";
        return 1;
    }

    std::cout << "Socket created successfully. FD: " << server_fd << '\n';
    std::cout << "PID: " << getpid() << '\n';

    // ===== bind =====
    sockaddr_in address{};

    address.sin_family = AF_INET;
    std::cout << "sin_family: " << address.sin_family << std::endl;
    address.sin_port = htons(8081);
    std::cout << "sin_port " << ntohs(address.sin_port) << std::endl;
    address.sin_addr.s_addr = htonl(INADDR_LOOPBACK); // INADDR_ANY entspreicht 0.0.0.0 
    std::cout << "s_addr " << ntohl(address.sin_addr.s_addr) << std::endl;

    // Bind socket to address
    if (bind(server_fd, reinterpret_cast<sockaddr*>(&address), sizeof(address)) == -1) {
        std::perror("bind");
        close(server_fd);
        return 1;
    }

    std::cout << "Socket bound to 127.0.0.1:8081" << std::endl;
    
    // ===== listen =====
    if (listen(server_fd, 5) == -1 ) {
        std::perror("listen");
        close(server_fd);
        return 1;
    }

    std::cout << "Listening... \n";
    

    // ===== accept =====
    bool running = true;
    while(running){
        sockaddr_in client_address{};
        socklen_t client_address_len = sizeof(client_address);

        // accept incoming connection
        int client_fd = accept(
            server_fd,
            reinterpret_cast<sockaddr*>(&client_address),
            &client_address_len
        );

        if (client_fd == -1) {
            std::perror("accept");
            break;
        }

        // Convert client IP to readable text
        char client_ip[INET_ADDRSTRLEN] {};

        if (inet_ntop(
            AF_INET,
            &client_address.sin_addr,
            client_ip,
            sizeof(client_ip)
            ) == nullptr) {
            std::perror("net_ntop of client_ip");
            close(client_fd);
            close(server_fd);
            return 1;
        }

        std::cout <<"Client connected !" << std::endl;
        std::cout << "CLIENT FD: " << client_fd << std::endl;
        std::cout << "Client IP: " << client_ip << std::endl;
        std::cout << "Client Port: " << ntohs(client_address.sin_port) << std::endl;

        timeval timeout{};
        timeout.tv_sec = 5;
        timeout.tv_usec = 0;

        if (setsockopt(
                client_fd,
                SOL_SOCKET,
                SO_RCVTIMEO,
                &timeout,
                sizeof(timeout)
            ) == -1) {
            std::perror("setsockopt");
            close(client_fd);
            continue;
        }

        // ===== reading =====
        std::string request_headers;

        ReadResult result = readHttpHeaders(
            client_fd,
            request_headers
        );

        if (result != ReadResult::Complete) {
            switch (result) {
                case ReadResult::TooLarge:
                    std::cerr << "HTTP headers too large" << std::endl;
                    break;
                
                case ReadResult::Closed:
                    std::cerr << "Client closed connection" << std::endl;
                    break;
                
                case ReadResult::Timeout:
                    std::cerr << "Request timeout" << std::endl;
                    break;

                default:
                    std::perror("recv");
                    break;
            }

            close(client_fd);
            continue;
        }

        std::cout << "Complete HTTP headers received: " << std::endl;
        std::cout << request_headers << std::endl;

        // ===== sending =====
        const std::string body = R"({"status":"ok"})";

        std::string response = "HTTP/1.1 200 OK\r\n";
        response += "Content-Type: application/json\r\n";
        response += "Content-Length: " + std::to_string(body.size()) + "\r\n";
        response += "\r\n";
        response += body;
        response += "Connection: close\r\n";

        size_t total_send = 0;

        while (total_send < response.size()) {
            ssize_t bytes_send = send(
                client_fd,
                response.data() + total_send,
                response.size() - total_send,
                MSG_NOSIGNAL
            );

            if (bytes_send == -1) {
                if(errno == EINTR) {
                    continue;
                }

                std::perror("send");
                break;
            }

            if (bytes_send == 0) {
                std::cerr << "No bytes send" << std::endl;
                break;
            }

            total_send += static_cast<size_t>(bytes_send);
        }

        std::cout << "Sent " << total_send << " bytes" << std::endl;

        close(client_fd);
    }
    // Close connection
    close(server_fd);

    return 0;
}