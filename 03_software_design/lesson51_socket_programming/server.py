import socket

server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server_socket.bind(("0.0.0.0", 5000))

server_socket.listen()

print("Server is waiting for connection...")

connection, address = server_socket.accept()

print("Connected by:", address)

data = connection.recv(1024)

message = data.decode()

print("Client says", message)

connection.send("Hello Client".encode())

connection.close()
server_socket.close()