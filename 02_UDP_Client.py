import socket 

Target_host = '192.168.101.5'
Target_port = 80

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto(bytes("aabbbccc",'utf-8'),(Target_host, Target_port))

data,adrr = client.recvfrom(1024)

print(data)