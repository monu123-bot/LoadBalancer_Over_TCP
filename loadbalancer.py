from socket import *
import socket
from _thread import *
server_socket = socket.socket()
host = '127.0.0.1'
port = 12345
threadCount = 0
try:
    server_socket.bind((host,port))
except socket.error as err:
    print(err)
    exit()
print("waiting for connections...")
server_socket.listen(5)
def client_thread(connection):
    connection.send(str.encode('Welcome to the server'))
    while True:
        data = connection.recv(2048)
        reply = "hello i m server "+data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()
while True:
    client,address = server_socket.accept()
    print('connected to '+str(address[0])+str(address[1]))
    start_new_thread(client_thread,(client,))
    threadCount+=1
    print('threaad number ',threadCount)