from Tkinter import *
import math


def read():
    with open('tile_map.txt') as map_:
        while True:
            c = map_.read(1)
            if not c:
              break
              
            print c
            
read()