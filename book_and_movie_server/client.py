from socket import socket


def main() -> None:
    s: socket = socket()
    s.connect(("localhost", 8001))
    s.send("test book,1,1000".encode())
    m = s.recv(1024).decode()
    print(m)
    s.close()

    s2: socket = socket()
    s2.connect(("localhost", 8002))
    s2.send("test book,1,1000".encode())
    m = s2.recv(1024).decode()
    print(m)
    s2.close()


if __name__ == "__main__":
    main()
