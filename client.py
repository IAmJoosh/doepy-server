import socket

MAX_SIZE_BYTES = 256
PORT = 9090
FORMAT = "utf-8"
IP_ADDRESS = socket.gethostbyname(socket.gethostname())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP_ADDRESS, PORT))

print(f"[*] {IP_ADDRESS} connected.")

message = "Hello, server! This is a really long message and I'm not really sure if this fits in the buffer. Let's see what happens."
client.send(message.encode(FORMAT))
