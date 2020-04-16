from tkinter import *
import threading,time
import math
import random
cake_dict=dict()
class Cake:
        def __init__(self):
                self.fat = random.randint(20,80)
                self.speed=10
                if random.randint(0,1):
                        if random.randint(0,1): #1.1
                                self.y = random.randint(0,root.winfo_vrootheight())
                                self.x = root.winfo_vrootwidth()
                                self.dirx =-1
                                self.diry =0
                        else:                   #1.0
                                self.y = random.randint(0,root.winfo_vrootheight())
                                self.x = 0
                                self.dirx =1
                                self.diry =0
                else:
                        if random.randint(0,1): #0.1
                                self.y = root.winfo_vrootheight()
                                self.x = random.randint(0,root.winfo_vrootwidth())
                                self.dirx =0
                                self.diry =-1
                        else:                   #0.0
                                self.y = 0
                                self.x = random.randint(0,root.winfo_vrootwidth())
                                self.dirx =0
                                self.diry =1
                self.dirx*=self.speed
                self.diry*=self.speed
                self.tag = field.create_oval(self.x,self.y,self.x+self.fat,self.y+self.fat,fill = "#cc9933")
                
        def move(self):
                field.move(self.tag,self.dirx,self.diry)
def move():
        speed=4
        global player,weight
        t=0
        while True:
                w = root.winfo_pointerx() - root.winfo_rootx() - field.coords(player)[0]
                h = root.winfo_pointery() - root.winfo_rooty() - field.coords(player)[1]
                if w==0:
                        w=0.000000000001
                a=math.atan(h/w)
                y=math.sin(a)*speed
                x=math.cos(a)*speed
                if w<0:
                        x=-x
                        y=-y
                #print(a/math.pi*180,x,y)
                time.sleep(0.02)
                field.move(player,x,y)
                field.update()
                need=False
                x,y,x1,y1 = field.coords(player)
                for i in cake_dict:
                        fx,fy,fx1,fy1 = field.coords(i)
                        if (x>root.winfo_vrootwidth() or x<0 or y<0 or y>root.winfo_vrootwidth()):
                                cake_dict.pop(i)
                                
                        cake_dict[i].move()
                for i in set(field.find_overlapping(x,y,x1,y1))-{player}:
                        if objs[i] == "food":
                                field.delete(i)
                                need=True
                        elif objs[i]=="medicine":
                                field.delete(i)
                                field.delete(player)
                                player = field.create_oval(x, y, 0.5*(x1+x), 0.5*(y1+y), fill="#44ab77")
                                x,y,x1,y1 = field.coords(player)
                        elif objs[i]=="cake":
                                fx,fy,fx1,fy1 = field.coords(i)
                                fat=(fx1-fx)/2
                                cake_dict.pop(i)
                                field.delete(i)
                                field.delete(player)
                                player = field.create_oval(x, y, x1+fat, y1+fat, fill="#44ab77")
                                x,y,x1,y1 = field.coords(player)
                                
                                
                if need:
                        field.delete(player)
                        player = field.create_oval(x, y, x1 + 1, y1 + 1, fill="#44ab77")
                        weight+=1
                        root.title("Съедено: "+str(weight)+"| Жирность: "+ str(int (x1-x)))
                t+=1
                if t%10==0:
                        temp = Cake()
                        objs[temp.tag]="cake"
                        cake_dict[temp.tag] = temp
                if t%333==0:
                        if int (x1-x)<500:
                                threading.Thread(target = fill_field_food).start()
                                add_medicine()
                        else:
                                break
                                
objs=dict()
                        
def fill_field_food(n=250):
        for i in range(n):
                x=random.randint(1,root.winfo_vrootwidth()-10)
                y=random.randint(1,root.winfo_vrootheight()-10)
                objs[field.create_oval(x,y,x+5,y+5,fill="black")] ="food"

                
def add_food():
        for i in range(3):
                x=random.randint(1,root.winfo_vrootwidth()-10)
                y=random.randint(1,root.winfo_vrootheight()-10)
                objs[field.create_oval(x,y,x+5,y+5,fill="black")] = "food"

def add_medicine():
        for i in range(3):
                x=random.randint(1,root.winfo_vrootwidth()-10)
                y=random.randint(1,root.winfo_vrootheight()-10)
                objs[field.create_oval(x,y,x+20,y+20,fill="green")] = "medicine"                
weight = 0
root=Tk()
root.state("zoomed")
x=random.randint(1,root.winfo_vrootwidth()-10)
y=random.randint(1,root.winfo_vrootheight()-10)
field=Canvas(bg="#a4b5d8",width=5552,height=5552)
field.place(x=0,y=0)
fill_field_food(1000)
player = field.create_oval(210,210,220,220,fill = "#44ab77")

threading.Thread(target=move).start()

root.mainloop()
