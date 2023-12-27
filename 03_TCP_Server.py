import socket 
import threading

bind_ip = "192.168.101.11" 
bind_port = 9998

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))
server.listen(5)

print(f'LIstening on {bind_ip} : {bind_port}')

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"Received: {request}")
    client_socket.send(bytes("ACK!",'utf-8'))
    client_socket.close()

while True:
    client, addr = server.accept()
    print(f"Accepted connection from: {addr}")

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()


#SUCESSFUL