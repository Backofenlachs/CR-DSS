import socket

with socket.create_connection(("127.0.0.1", 8081)) as client:
    client.sendall(b"GET /health HTTP/1.1\r\n")
    print(client.recv(1024))