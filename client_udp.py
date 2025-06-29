import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input() + "\n"
    client.sendto(msg.encode(),('172.31.224.197', 990))
    msg, src = client.recvfrom(1024)
    print(src[0], src[1], msg.decode())