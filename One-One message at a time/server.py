import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host="192.168.20.68"
port=9999

s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print("Established a connection with host",addr)
while True:
        data=c.recv(1024).decode()
        print("Message from host:- ",data)
        inp=(input("Your message:- "))
        c.send(str.encode(inp))
        print()
c.close()
s.close()
