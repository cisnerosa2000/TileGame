from Tkinter import *
import math

root = Tk()
root.title('Tiles')
canvas = Canvas(root)
canvas.config(width=1000,height=600)
#20 x 12


coord1 = [0,0]
coord2 = [50,50]


color = 'red'

dirt_tile = PhotoImage(file='dirt.gif')



def read():
    with open('tile_map.txt') as tilemap:
        while True:
            c = (tilemap.read(1))
            if not c:
                break
                
           
           
            if c == """\n""":
               coord1[1] += 50
               coord2[1] += 50
               
               
               coord1[0] = 0
               coord2[0] = 50
               
               
               
               make = False
            elif c == '0':
                color = 'red'
                make = True
            elif c == '1':
                color = 'green'
                make = True
                
            
            if make == True:
                rect = canvas.create_rectangle(coord1[0],coord1[1],*coord2,fill=color)
        
                coord1[0] += 50
                coord2[0] += 50          
            
read()        
        
               




canvas.pack()
root.mainloop()