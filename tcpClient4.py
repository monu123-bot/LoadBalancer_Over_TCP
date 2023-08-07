from socket import *
import socket
client_socket = socket.socket(family=AF_INET,type=SOCK_STREAM)
client_socket.connect(('127.0.0.1',12345))
payload = 'Hey server this is message from client 4'
try:
    while True:
        client_socket.send(payload.encode('utf-8'))
        data = client_socket.recv(1024)
        print(data)
        more = input('want to send more data to the server... ? Y/N :')
        if more=='y':
            payload = input('enter data :')
        else:
            break
except KeyboardInterrupt :
    print('exited by user')