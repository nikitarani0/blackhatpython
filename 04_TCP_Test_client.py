import socket
Target_host = '10.0.2.15'
Target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((Target_host,Target_port))

client.send(bytes("ABCSD",'utf-8'))

response = client.recv(1024)

print(response.decode())