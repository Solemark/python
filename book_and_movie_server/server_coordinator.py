from socket import socket


class ServerCoordinator:
    def __init__(self) -> None:
        self.ADDRESS: str = "localhost"
        self.PORT: int = 8000
        self.CONNECTIONS: int = 5

        self.SERVER = socket()
        self.SERVER.bind((self.ADDRESS, self.PORT))
        self.SERVER.listen(self.CONNECTIONS)

        print(f"Listening on {self.ADDRESS}:{self.PORT}")

        self.__run_server()

    def __run_server(self) -> None:
        while True:
            sock, addr = self.SERVER.accept()
            print(f"Incoming message from {addr}")

            m: list[str] = sock.recv(1024).decode().split(",")
            r: str = self.__send_message(m)

            sock.send(r.encode())
            sock.close()

    def __send_message(self, m: list[str]) -> str:
        response: str = ""
        match m[0]:
            case "B":
                response = self.__send_book(m)
            case "M":
                response = self.__send_movie(m)
        return response

    def __send_book(self, m: list[str]) -> str:
        s: socket = socket()
        s.connect(("localhost", 8001))
        s.send(f"{m[1]},{m[2]},{m[3]}".encode())
        res = s.recv(1024).decode()
        s.close()
        return res

    def __send_movie(self, m: list[str]) -> str:
        s: socket = socket()
        s.connect(("localhost", 8002))
        s.send(f"{m[1]},{m[2]},{m[3]}".encode())
        res = s.recv(1024).decode()
        s.close()
        return res


if __name__ == "__main__":
    ServerCoordinator()
