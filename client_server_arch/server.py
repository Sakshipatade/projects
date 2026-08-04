import socket


# create a socket
server_socket = socket.socket()
# Telling client that use 3000 to connect with me..
server_socket.bind(('localhost',3000))
server_socket.listen(1)

print('server is waiting on port 3000....')


conn, addr = server_socket.accept()
print(f'connected with {addr}')

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print('client: ', data)
    # conn.send(f'Received: {data}'.encode())

conn.close()
server_socket.close()


# We can write it using the context managers so we don't need to close the connection manually

import socket

with socket.socket() as server_socket:
    server_socket.bind(('localhost', 8080))
    server_socket.listen()

    print('I am ready and listeing on port 8080')

    conn, addr = server_socket.accept()
    print(f'Client address: {addr}')

    while True:
        data = conn.recv(1024).decode()
        if not data:
            print('connection closed')
            break
        print(f'Client data: {data}')
