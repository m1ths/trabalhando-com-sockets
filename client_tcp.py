import socket



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('172.31.224.197', 990))

while True:
    msg = input() + "\n"
    client.send(msg.encode())
    print(client.recv(1024).decode())