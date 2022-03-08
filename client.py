import socket


soc_socket = socket.socket()
soc_socket.connect(('localhost',5028))
while True:
    message = input(":: ")
    soc_socket.send(bytes(message,'utf-8'))
    print(soc_socket.recv(1024).decode())

soc_socket.close()
