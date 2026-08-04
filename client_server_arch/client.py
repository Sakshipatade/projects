import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 3000))

while True:
    my_msg = input('Ask: ')
    client_socket.send(my_msg.encode())

    # response = client_socket.recv(1024).decode()
    # print('Server: ', response)
    
    if my_msg.lower() == 'exit':
        print('closing client connection.')
        break


client_socket.close()


# We can write it using the context managers so we don't need to close the connection manually
import socket

with socket.socket() as client_socket:
    client_socket.connect(('localhost', 8080))

    while True:
        msg = input('ask: ')
        client_socket.send(msg.encode())

        if msg.strip().lower() == 'exit':
            print('connection closed..')
            break