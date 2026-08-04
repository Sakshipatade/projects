import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 3000))

while True:
    my_msg = input('Ask: ')
    client_socket.send(my_msg.encode())

    response = client_socket.recv(1024).decode()
    print('Server: ', response)