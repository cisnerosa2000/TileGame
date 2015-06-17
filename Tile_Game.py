from Tkinter import *
import math

root = Tk()
root.title('Tiles')
canvas = Canvas(root)
canvas.config(width=1000,height=600)
#20 x 12


coords = [0,0]




dirt_tile = PhotoImage(file='dirt.gif')
sky_tile = PhotoImage(file='sky.gif')
door_tile = PhotoImage(file='door.gif')



def read():
    with open('tile_map.txt') as tilemap:
        while True:
            c = (tilemap.read(1))
            if not c:
                break
                
           
           
            if c == """\n""":
               coords[1] += 50
               coords[0] = 25
               make = False
               
            elif c == '0':
                tile = sky_tile
                make = True
            elif c == '1':
                tile = dirt_tile
                make = True
            elif c == '3':
                tile = door_tile
                make = True
            
            if make == True:
                tile = canvas.create_image(*coords,image=tile)
        
                coords[0] += 50
                         
            
read()        
        
               




canvas.pack()
root.mainloop()