from Tkinter import *
import math

root = Tk()
root.title('Tiles')
canvas = Canvas(root)
canvas.config(width=600,height=400)

coord1 = [0,0]
coord2 = [50,50]


color = 'red'



def read():
    with open('tile_map.txt') as tilemap:
        while True:
            c = int(tilemap.read(1))
            if not c:
                break
            
        
            if c == '0':
                color = 'red'
            elif c == '1':
                color = 'green'
            else:
                color = 'purple'
            
        
            canvas.create_rectalnge(coord1[0],coord1[1],*coord2,fill=color)
        
            coord1[0] += 50
            coord1[1] += 50
        
            coord2[0] += 50
            coord2[1] += 50
          
read()        
        
               




canvas.pack()
root.mainloop()