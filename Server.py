import socket


server = socket.socket()


server.bind(('localhost',5028))

server.listen(5)

while True:
    c, adress = server.accept()
    print(' : ' +c.recv(1024).decode())
    while True:
        message = input(' :: ')
        c.send(bytes(message,'utf-8'))
        print(' '+c.recv(1024).decode())
c.close()
