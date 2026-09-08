import socket


def run_client(
    host: str,
    port: int
):

    with socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    ) as sock:

        sock.connect(
            (host, port)
        )

        sock.sendall(
            b"hello"
        )

        response = sock.recv(
            1024
        )

        return response.decode()