# from socket import *
# import socket
# import select
# import sys
# from _thread import *
# client_socket = socket.socket(family=AF_INET,type=SOCK_STREAM)
# client_socket.connect(('127.0.0.1',80))
# name = input('Enter your name')
# client_socket.send(name.encode())
# def handleSend(client):
#     while True:
#         data = f'{name}:{input("Enter message to send :")}'
#         client.send(data.encode())


# def handleRecv(client):
#     while True:
#         try:
#             data = client.recv(2048).decode()
#             print(data)
#         except:
#             client_socket.close()
#             break
# a = ''
# start_new_thread(handleSend,(client_socket,))
# start_new_thread(handleRecv,(client_socket,))

# import required modules
import socket
import threading


HOST = '127.0.0.1'
PORT = 80



# Creating a socket object
# AF_INET: we are going to use IPv4 addresses
# SOCK_STREAM: we are using TCP packets for communication
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



def connect():

    # try except block
    try:

        # Connect to the server
        client.connect((HOST, PORT))
        print("Successfully connected to server")
        # add_message("[SERVER] Successfully connected to the server")
    except:
        print("Unable to connect to server", f"Unable to connect to server {HOST} {PORT}")

    username = input('Enter username :')
    if username != '':
        client.sendall(username.encode())
    else:
        print("Invalid username", "Username cannot be empty")
    threading.Thread(target=send_message, args=(client, )).start()
    threading.Thread(target=listen_for_messages_from_server, args=(client, )).start()
    

    

def send_message(client):
    while 1:
        message  =  input('Enter message :')
        if message!='':
            client.sendall(message.encode())
        else:
            print("empty message ")
            exit(0)



def listen_for_messages_from_server(client):

    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            

            print(message)
            
        else:
            print("Error", "Message recevied from client is empty")

# main function
def main():

    connect()
    
if __name__ == '__main__':
    main()