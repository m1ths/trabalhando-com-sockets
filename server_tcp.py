import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 4433))
server.listen(5)

print("Servidor TCP rodando na porta 990...")

while True:
    client_socket, addr = server.accept()
    print(f"Conexão de {addr} aceita!")
    client_socket.send(b"Ola, cliente!\n")
    client_socket.close()
