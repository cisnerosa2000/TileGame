from Tkinter import *
from ast import literal_eval
import random

root = Tk()
root.title('Tiles')
canvas = Canvas(root)
canvas.config(width=1000,height=600)
#20 x 12


coords = [0,0]

#make gun, ammo counter, and enemies
#when enemy dies, drop ammo

# TODO:
# Make ammopack sprite
# add ammopack to list of usable blocks
# I already added functionality of ammopacks in loop function


dirt_tile = PhotoImage(file='dirt.gif')
sky_tile = PhotoImage(file='sky.gif')
door_tile = PhotoImage(file='door.gif')
ammo_tile = PhotoImage(file='ammopack.gif')
zom_tile = PhotoImage(file='zom.gif')


Right = PhotoImage(file='Right.gif')
Left = PhotoImage(file='Left.gif')
bulletimg = PhotoImage(file='bullet.gif')

global first_time
global sprite_list
first_time = True
sprite_list = []
class Enemy(object):
    def __init__(self,kind,coords,velocity):
        self.kind = kind
        self.coords = coords
        self.velocity = velocity
    def make(self):
        global sprite_list
        global first_time
        if self.kind == 'zom':
            self.sprite = canvas.create_image(*self.coords,image=zom_tile,tags="Enemy")
            self.health = 200
            sprite_list.append(self.sprite)
            
            canvas.move(self.sprite,0,-30)
        if first_time == True:
            self.moveloop()
            first_time = False
            
    def moveloop(self):
        global bullet_list
        
        for sprite in sprite_list:
            ##update health bar
            try:
                canvas.delete(self.healthrect)
            except AttributeError:
                pass
            ##update health bar
    
            #### Gravity
            self.bbox = canvas.bbox(sprite)
            self.colliding = canvas.find_overlapping(*self.bbox)
        
            self.collide_list = []
        
            for i in self.colliding:
                c = canvas.gettags(i)
                self.collide_list.append(c)
        
            if ("Collide",) not in self.collide_list:
                canvas.move(sprite,0,5)
        
        
            ### Gravity
        
            ### detect hits
            try:
                if ("bullet",) in self.collide_list:
                    self.health -= 5
                    
                    
                    
                
                            
            except:
                pass
                    
                        
                
                    
                    
            if self.health <= 0:
                canvas.delete(sprite)
                sprite_list.remove(sprite)
                
                
            ### delete bullets  
            for item in self.colliding:
                if canvas.gettags(item) == ('bullet',):
                    canvas.delete(item)
                        
                    index = bullet_list.index(item)
                    velocity_list.pop(index)
                    bullet_list.remove(item)
            ### delete bullets
        
        
            ### detect hits
        
            #Necessary to fix bug where sky tiles overlapped the zom and blocked it out
            try:
                canvas.tag_raise(sprite)
            except NameError:
              pass
            #Necessary to fix bug where sky tiles overlapped the zom and blocked it out
        
        
            ### tracks player
            try:
                if abs(canvas.coords(player_one.P1)[0] - canvas.coords(sprite)[0]) <= 900 and abs(canvas.coords(player_one.P1)[1] - canvas.coords(sprite)[1]) < 800 :
                    if canvas.coords(player_one.P1)[0] + 30 < canvas.coords(sprite)[0]:
                        canvas.move(sprite,-1,0)
                    elif canvas.coords(player_one.P1)[0] -30 > canvas.coords(sprite)[0]:
                        canvas.move(sprite,1,0)
            except :
                pass
        
        
        
            ### tracks player
        
        
            ###creates health bar
        
            try:
                hb = canvas.coords(sprite)
                self.healthrect = canvas.create_rectangle(hb[0]-30,hb[1]-60,hb[0]+self.health-30,hb[1]-50,fill="red")
            except IndexError:
                pass
        
        
            ###creates health bar
        

            
        root.after(10,self.moveloop)
        
        
        


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
                tileimg = sky_tile
                make = True
            elif c == '1':
                tileimg = dirt_tile
                make = True
            elif c == '3':
                tileimg = door_tile
                make = True
            elif c == '4':
                tileimg = ammo_tile
                make = True
            elif c == 'Z':
                tileimg = sky_tile
                zom = Enemy(kind='zom',coords=[coords[0],coords[1]],velocity=0)
                zom.make()
            
            if make == True:
                tile = canvas.create_image(*coords,image=tileimg)
                if c == '1':
                    canvas.itemconfig(tile,tags="Collide")
                elif c == '3':
                    canvas.itemconfig(tile,tags="Door")
                elif c == '4':
                    canvas.itemconfig(tile,tags="ammopack")
                
                    
        
                coords[0] += 50
                         
            
read()
bullet_list = []
velocity_list = []

class Player_1(object):
    def __init__(self,coords,velocity,ammo,health,alive):
        self.coords = coords
        self.velocity = velocity
        self.ammo = ammo
        self.health = health
        self.alive = alive
    def make(self):
        self.P1 = canvas.create_image(*self.coords,image=Right)
    def move_right(self):
        self.velocity += 5
    def move_left(self):
        self.velocity -= 5
    def jump(self):
        canvas.move(self.P1,0,-50)
    def fire(self):
        self.bullet = canvas.create_image(*canvas.coords(self.P1),image = bulletimg,tags="bullet")
        if "right" in canvas.gettags(self.P1):
            self.bullet_velocity = 10
        else:
            self.bullet_velocity = -10
        bullet_list.append(self.bullet)
        velocity_list.append(self.bullet_velocity)
    def bullet_loop(self):
        global bullet_list
        
        try:
            for bullet in bullet_list:
                for velocity in velocity_list:
                    canvas.move(bullet,velocity,0)
                    
                try:
                    
                    if canvas.coords(bullet)[0] > 1000 or canvas.coords(bullet)[0] < 0:
                        canvas.delete(bullet)
                        bullet_list.remove(bullet)
                        velocity_list.remove(velocity)
                            
                except:
                    pass
                        
        
            
        except NameError:
            self.bullet = None
            
        
            
        root.after(1,self.bullet_loop)
        







        


player_one = Player_1(coords=[75,475],velocity=0,ammo = 15,health = 100,alive=True)
player_one.make()
player_one.bullet_loop()


thing = True
def victory():
    global thing    
    if thing == True:
        print "Win!"
        
        thing = False
        
        
def textbox():
    global text
    
    text = Text(root)
    
    text.config(state=DISABLED)
    text.config(width=41,height=4,bg="gray")
    
    
    text.place(x=710,y=0)
textbox()

num = 0       
in_goal = False
hurt = False

def loop():
    global num
    global distance
    global collision_list
    global ec
    global in_goal
    global jumps
    global text
    global p1_sprite
    global hurt
    
    #erase healthbar so it can be redrawn
    try:
        canvas.delete(player_one.healthbar)
        
    except AttributeError:
        pass
    try:
        canvas.delete(player_one.health_outline)
    except AttributeError:
        pass

    
    #erase healthbar so it can be redrawn
    
    
    ### collision ###
    playerbbox = canvas.bbox(player_one.P1)
    colliding = canvas.find_overlapping(*playerbbox)
    collision_list = []

   
    for i in colliding:
        a = canvas.gettags(i)
        collision_list.append(a)


   
    old_coords = 1
    if ("Collide",) not in collision_list:
        canvas.move(player_one.P1,0,num)
        num += .49
        
        
        
    else:
        
        num = 0
        jumps = 0
      
   
    if ("Door",) in collision_list:
        global text
        
        if in_goal == False:
            text.config(state=NORMAL)
            text.insert(INSERT,"You have reached the Goal!")
            text.config(state=DISABLED)
            in_goal = True

    
        
        
        
        
        
        
        
    
   
    
    
    
    elif ("ammopack",) in collision_list and int(player_one.ammo) < 20:
        player_one.ammo += .1
        for block in colliding:
            if canvas.gettags(block) == "ammopack":
                canvas.delete(block)
        
        
        
         
    elif ("Enemy",) in collision_list and player_one.alive == True:
        
        try:
            player_one.health -= 10
            canvas.itemconfig(player_one.healthbar,fill="red")
        except:
            pass
    
    
    
    if canvas.coords(player_one.P1)[0] > 50 and canvas.coords(player_one.P1)[0] < 950 and in_goal == False:
        canvas.move(player_one.P1,int(player_one.velocity),0)
    else:
        player_one.velocity *= -1
        canvas.move(player_one.P1,int(player_one.velocity),0)
    
        
    
    
    
    ### collision ###
    
    
    if player_one.velocity < 1 and player_one.velocity > -1:
        player_one.velocity = 0
    
   
    if player_one.velocity > 0:
        player_one.velocity -= .1
        canvas.itemconfig(player_one.P1,image=Right,tags="right")
    

    elif player_one.velocity < 0:
        player_one.velocity += .1
        canvas.itemconfig(player_one.P1,image=Left,tags="left")
        
        
    
        
   
    if player_one.velocity > 40:
        player_one.velocity = 40
    elif player_one.velocity < -40:
        player_one.velocity = -40
        
   
    text.config(state=NORMAL)
    text.delete(1.0,END)
    text.insert(INSERT,"Health: %s" % int((player_one.health)))
    text.insert(INSERT,"\n")
    text.insert(INSERT,"Ammo: %s" % int((player_one.ammo)))
    
    
    
    text.config(state=DISABLED)
    

    if int(player_one.health) <= 0:
        player_one.alive = False
      
        
        
    
  
    
    
    
        
    

    
    
    
    
    
    try:
        if player_one.health >= 0:
            hb = canvas.coords(player_one.P1)
            player_one.healthbar = canvas.create_rectangle(hb[0]-30,hb[1]-60,hb[0]+player_one.health-30,hb[1]-50,fill="green")
            player_one.health_outline = canvas.create_rectangle(hb[0]-30,hb[1]-60,hb[0]+70,hb[1]-50)
    except IndexError:
        pass
    
    
    
    root.after(1,loop)
            
loop()         
                   



def right_move(event):
    global jumps
    if ("Collide",) in collision_list and player_one.alive == True or jumps <= 1 and player_one.alive == True:
        player_one.move_right()
        jumps += 1
        
def left_move(event):
    global jumps
    if ("Collide",) in collision_list and player_one.alive == True or jumps <= 1 and player_one.alive == True:
        player_one.move_left()
        jumps += 1
        
def jump(event):
    
    if ("Collide",) in collision_list and player_one.alive == True:
        player_one.jump()
        

def fire(event):
    
    
    
    if int(player_one.ammo) > 0 and player_one.alive == True:
        player_one.ammo -= 1
        player_one.fire()


root.bind('<Right>',right_move)
root.bind('<Left>',left_move)
root.bind('<Up>',jump)
root.bind('<Down>',fire)


canvas.pack()
root.mainloop()