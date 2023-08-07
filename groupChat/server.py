
# from socket import *
# import socket
# from _thread import *
# import sys
# server = socket.socket(family=AF_INET,type=SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# ip = sys.argv[1]
# port = int(sys.argv[2])
# print(ip,port)

# server.bind((ip,port))
# clientList = []
# all_clients = dict()
# server.listen(100)
# def remove(client):
#     clientList.remove(client)


# def broadcast(client,message):
#     print('inside booad',client,message)
#     for node in clientList:
#         # print(node,client)
#         if node!=client:
#             try:
#                 # print('inside broadcast message sending to  ',node)
#                 node.send(str.encode(message))
#             except:
#                 node.close()
#                 remove(node)

# def createNewThread(client):

#     client.send(str.encode('Welcome to server'))
#     try:

#         msg = client.recv(2048).decode()
#         for c in all_clients:
#             c.send(msg)
#     except ConnectionResetError as err:
#         print(' discarded ',err)


#     # while True:
#     #     try:
#     #         message = client.recv(2048)
#     #         if message:
#     #             print(f'Message from {addr}',message)
#     #             messagetoSend = "<"+addr[0] +">" + str(message)
                
#     #             client.send(str.encode('message send successfully '))
#     #             broadcast(client,messagetoSend)
#     #         else:
#     #             remove(client)
                
#     #     except:
#     #         continue
# l = 0
# while True:
#     try:
#         print('Waiting for connection.....')
#         client,addr =  server.accept()
#         print(f'Connected to {client}  ')
#         try:
#             name = client.recv(2048).decode()
#             l+=1
#             print('number of connected users ',l)
#             all_clients[client] = name

#             start_new_thread(createNewThread,(client,))
#         except ConnectionResetError  as err:
#             print('Discarded',err)
#     except KeyboardInterrupt:
#         break
    


# server.close()
    

# Import required modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 80 # You can use any port between 0 to 65535
LISTENER_LIMIT = 5
active_clients = [] # List of all currently connected users

# Function to listen for upcoming messages from a client
def listen_for_messages(client, username):

    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            
            final_msg = username + '~' + message
            send_messages_to_all(final_msg)

        else:
            print(f"The message send from client {username} is empty")


# Function to send message to a single client
def send_message_to_client(client, message):

    client.sendall(message.encode())

# Function to send any new message to all the clients that
# are currently connected to this server
def send_messages_to_all(message):
    
    for user in active_clients:

        send_message_to_client(user[1], message)

# Function to handle client
def client_handler(client):
    
    # Server will listen for client message that will
    # Contain the username
    while 1:

        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            prompt_message = "SERVER~" + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break
        else:
            print("Client username is empty")
            

    threading.Thread(target=listen_for_messages, args=(client, username, )).start()

# Main function
def main():

    # Creating the socket class object
    # AF_INET: we are going to use IPv4 addresses
    # SOCK_STREAM: we are using TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Creating a try catch block
    try:
        # Provide the server with an address in the form of
        # host IP and port
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    # Set server limit
    server.listen(5)

    # This while loop will keep listening to client connections
    while 1:

        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")

        threading.Thread(client_handler, (client, )).start()


if __name__ == '__main__':
    main()





