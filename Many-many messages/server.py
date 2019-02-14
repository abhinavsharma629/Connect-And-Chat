import socket
import os
import threading
from queue import Queue
no_of_threads=2
threads=[1,2]
q=Queue()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host="192.168.20.68"
port=9999

s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print("Successfully connected to client with address:- ",addr)
print()
while True:
        def work():
                while True:
                        x=q.get()
                        if(x==1):
                                data=c.recv(1024).decode()
                                while data:
                                        print("Message from host:- ",data)
                                        data=c.recv(1024).decode()
                                
                        if(x==2):
                                inp=(input("Your message:- "))
                                while inp:
                                        c.send(str.encode(inp))
                                        inp=(input("Your message:- "))
                        q.task_done()
        def create():
                for x in threads:
                        q.put(x)
                q.join()

        
        for _ in range(no_of_threads):
                t=threading.Thread(target=work)
                t.daemon=True
                t.start()
        create()
        
c.close()
s.close()
