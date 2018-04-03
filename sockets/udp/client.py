import socket

PORT = 3333
HOST = '127.0.0.1'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = "Hello UDP!".encode()
s.sendto(data, (HOST, PORT))
print("Send: %s to %s : %s " %(data, HOST, PORT))

s.close()

