import socket


# create a socket
server_socket = socket.socket()
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
    conn.send(f'Received: {data}'.encode())

conn.close()
server_socket.close()