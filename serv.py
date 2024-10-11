import socket
import threading


class Server:
    def __init__(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv.bind(("0.0.0.0", 8080))
        self.serv.listen(5)
        self.from_client = []

    def start(self):
        while True:
            conn, addr = self.serv.accept()
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

    def handle_client(self, conn, addr):
        while True:
            data = conn.recv(4096).decode()
            if not data:
                break
            print(f"{addr}: {data}")
            conn.send(
                "\n".join(
                    [f"{id}.: {ad}.: {da}" for id, ad, da in self.from_client]
                ).encode()
            )
            self.from_client.append((len((self.from_client)), addr, data))
        conn.close()
        print("client disconnected")

    def __del__(self):
        self.serv.close()


serv = Server()

try:
    print("Server started")
    serv.start()
except KeyboardInterrupt:
    print("Server stopped")
    del serv
