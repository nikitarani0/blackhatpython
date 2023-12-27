import socket 

server_host = '192.168.101.11'
server_port = 80
server_adr = (server_host, server_port)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(server_adr)
while True:
    data,adrr = server.recvfrom(1024)

    print("Receieved msg: ",data.decode())
    