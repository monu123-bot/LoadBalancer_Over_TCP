import threading
from socket import *
import socket

Host = '127.0.0.1'
port= 80

client = socket.socket(family=AF_INET,type=SOCK_STREAM)
client.connect((Host,port))
def send_msg(client,name):
    while 1:
        mas = input('Enter message :')
        if mas!='':
            client.sendall(mas.encode())
        else:
            print(' cannot send empty message ')
            exit(0)
    
def check_for_comingmsg(client,name):
    while 1:
        mas = client.recv(2048).decode()
        if mas!='':
            print(mas)
        else:
            continue
while 1:
    name = input("Enter name :")
    if name!='':
        client.send(name.encode())
    else:
        print(' client name can not be empty ..')

    threading.Thread( target= send_msg,args=(client,name,)).start()
    threading.Thread(target=check_for_comingmsg,args=(client,name,)).start()

    