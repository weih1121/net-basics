import socket

HOST = '127.0.0.1'
PORT = 3333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
print("Connecte %s : %d OK" %(HOST, PORT))
data = s.recv(1024)
print("Receive: {}".format(data.decode()))
s.close()