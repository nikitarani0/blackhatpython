import socket
Target_host = 'google.com'
Target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((Target_host,Target_port))

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(1024)

print(response)

#SUCCESFUL