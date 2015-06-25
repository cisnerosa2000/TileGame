#!/usr/bin/env python
import socket 
import sys

port = 8888
backlog = 1
size = 1024

s = None
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind(('',port)) 
    s.listen(backlog) 




except socket.error, (value,message):
    if s:
        s.close()
        print "Could not open socket: " + message
        sys.exit(1)   
    

while 1: 
    client, address = s.accept() 
    data = client.recv(size) 
    while data:
        try:
            with open('enemy_coords.txt','w') as enemycoords:
                enemycoords.write(data)
            with open('my_coords.txt','r') as mycoords:
                my_coordinates = mycoords.read()
                s.send(my_coordinates)
        except socket.error:
            print "Client disconnected"
            break
        
            
            
        
    client.close()