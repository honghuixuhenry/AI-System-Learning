import socket

client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client_socket.connect(("0.0.0.0", 5000))

print("Connected to server.")

client_socket.send(b"Hello Server")

data = client_socket.recv(1024)

message = data.decode()

print("Server says:", message)

client_socket.close()