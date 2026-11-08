#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string>
#include <cerrno>

/**
 * POISY-Socket-API basics:
 * 
 * socket():   // erzeugt einen kommunikations endpunkt und gibt den file descriptor zurück.
 * bind():      // verknüpft einen socket mit einer netzwerkadress und portnummer
 * accept():    // nimmt die erste anstehende verbindungsanfrage entgegen und erstellt einen komplett neuen socket pro verbindung.
 * close():     // gibt den socket-descriptor frei und leitet das schließen der eigentlichen netzwerverbindung ein.
 *
 * g++ command:
 * g++ -Wall -Wextra -Wpedantic src/main.cpp -o system-service
 */

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
     * 0 => satandard input
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
    std::cout << "sin_family: " << ntohs(address.sin_family) << " | little edian: " << address.sin_family << std::endl;
    address.sin_port = htons(8081);
    std::cout << "sin_port " << ntohs(address.sin_port) << " | little edian:" << address.sin_port << std::endl;
    address.sin_addr.s_addr = htonl(INADDR_LOOPBACK); // INADDR_ANY entspreicht 0.0.0.0 
    std::cout << "s_addr " << ntohs(address.sin_addr.s_addr) << " | little edian:" << address.sin_addr.s_addr << std::endl;

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
        close(server_fd);
        return 1;
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


    // ===== reading =====
    char buffer[1024]{};

    ssize_t bytes_recieved = recv(
        client_fd,
        buffer,
        sizeof(buffer),
        0
    );

    if (bytes_recieved == -1) {
        std::perror("recv");
    } else if (bytes_recieved == 0) {
        std::cout << "Client closed the connection" << std::endl;
    } else {
        std::cout << "Received " << bytes_recieved << " bytes: " << std::endl;

        std::cout.write(buffer, bytes_recieved) << std::endl;
    }

    // ===== sending =====
    const std::string body = R"({"status":"ok"})";

    std::string response = "HTTP/1.1 200 OK\r\n";
    response += "Content-Type: application/json\r\n";
    response += "Content-Length: " + std::to_string(body.size()) + "\r\n";
    response += "\r\n";
    response += body;

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

    // Close connection
    close(client_fd);
    close(server_fd);

    return 0;
}