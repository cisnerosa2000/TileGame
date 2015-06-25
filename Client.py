#!/usr/bin/env python
import socket 
import sys

host = 'localhost'
port = 8888
size = 1024 

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect((host,port)) 
except socket.error, (value,message): 
    if s: 
        s.close() 
    print "Could not open socket: " + message 
    sys.exit(1)

while 1:
    data = s.recv(size) 
    while True:
        with open('enemy_coords.txt','w') as enemycoords:
            enemycoords.write(data)
        with open('my_coords.txt','r') as mycoords:
            my_coordinates = mycoords.read()
            s.send(my_coordinates)
    

s.close() 
