import socket

HOST = '0.0.0.0'
PORT = 3333

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
    data, addr = s.recvfrom(1024)
    print("Receive %s from %s" %(data.decode(), addr))

s.close()