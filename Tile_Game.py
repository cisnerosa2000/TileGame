from Tkinter import *
import math


def read():
    with open('tile_map') as map_:
        while True:
            c = map_.read(1)
            if not c:
              print "End of file"
              break
              
            print "Read a character:", c
            
read()