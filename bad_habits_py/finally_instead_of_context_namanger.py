import socket


def finally_instead_of_context_manager(host: str, port: str) -> None:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.sendall(b"Hello, World!")
    finally:
        s.close()


def properly_use_context_manager(host: str, port: str) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"Hello, World!")
