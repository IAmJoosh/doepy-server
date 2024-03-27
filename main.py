import socket
import threading

MAX_SIZE_BYTES = 64
PORT = 9090
FORMAT = "utf-8"
IP_ADDRESS = socket.gethostbyname(socket.gethostname())


class Server:
    def __init__(self, address, port, max_size_bytes, encoding_format):
        self.address = address
        self.port = port
        self.max_size_bytes = max_size_bytes
        self.encoding_format = encoding_format

    def serve(self):
        _server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _server.bind((self.address, self.port))
        _server.listen()
        print(f"[*] Listening as {self.address}:{self.port}")
        while True:
            client, address = _server.accept()
            _thread = threading.Thread(target=self.handle_request, args=(client, address), daemon=True)
            _thread.start()
            self.handle_request(client, address)
            print(f"[*] {address} connected.")

    def handle_request(self, client, address):
        while (received := client.recv(self.max_size_bytes).decode(self.encoding_format)) != "":
            print(f"[+] Received: {received}" + f" from {address}" if address else "")


if __name__ == "__main__":
    server = Server(IP_ADDRESS, PORT, MAX_SIZE_BYTES, FORMAT)
    server.serve()
