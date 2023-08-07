import threading
from socket import *
import socket
import sys

Host = sys.argv[1]
Port = int(sys.argv[2])

client_list = dict()

server_socket = socket.socket(family=AF_INET,type=SOCK_STREAM)

server_socket.bind((Host,Port))

server_socket.listen(5)
 

database = dict()

def broadcast(client,message):
    for name,node in client_list.items():
        if node!=client:
            node.sendall(str.encode(message))
def save(msg):
    
    method = msg[:3]
    rem_msg = msg[3:].split('-')
    
    key = rem_msg[1]
    if method=='PUT':
        value = rem_msg[2]
        database[key] = value
        return 'value added successfully..'
    elif method=='GET':
        if key in database:
            return database[key]
        else:
            return 'Key not present..'
    elif method=='DEL':
        if key in database:
            del database[key]
            return 'successfully deleted'
        else:
            return 'Key not present...'
    else:
        return 'request syntax in invalid..'
    
    

def checkTheIncomingMessage(client,name):

    while 1:
        
            msg = client.recv(2048).decode('utf-8')
            
            if msg!='':
                res = save(msg)
                client.sendall(str.encode(res))
                # broadcast(client,str(name) + ':' + msg)
            
            else:

                print("message sent is empty")


def handleClient(client):

    while 1:
        
        name = client.recv(2048).decode('utf-8')
        if name !='':
            client_list[name] = client
            joiningMsg = str(name) + " joined the chat "
            broadcast(client,joiningMsg)
            break
        else:

            print(' No name from client ')
            

    threading.Thread(target=checkTheIncomingMessage,args=(client,name,)).start()





while True:

    print('Waiting for new connection....')
    client,addr = server_socket.accept()
    print("creating thread for new client .....")
    
    
    threading.Thread(target=handleClient,args=(client,)).start()



