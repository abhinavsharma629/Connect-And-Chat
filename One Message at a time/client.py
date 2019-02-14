import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host="192.168.20.68"
port=9999

s.connect((host,port))
print("You may start chatting")
while True:
    inp=(input("Your message:- "))
    s.send(str.encode(inp))
    data=s.recv(1024).decode()
    print("Message from server:- ",data)
    print()

s.close()
