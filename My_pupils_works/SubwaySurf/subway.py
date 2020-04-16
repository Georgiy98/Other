
from tkinter import*
from random import randint
import time
trains=[]

def procces():
    for i in trains:
        game_area.delete(i)
        trains.remove(i)
    for i in coins:
        game_area.delete(i)
        coins.remove(i)
    for i in info_frame.place_slaves():
        i.destroy()
    t=0
    hp=3
    train_amount=0
    coin_amount=0
    heart_labels=[]
    need_break=False
    Label(info_frame,text=chr(169)+":",fg="black",bg="yellow",font="Arial 15 bold").place(x=10,y=10)
    coin_Label=Label(info_frame,text=0,fg="black",bg="white",font="Arial 15 bold")
    coin_Label.place(x=40,y=10)
    for i in range(3):
        temp = Label(info_frame,text=chr(9829),fg="red",bg="white",font="Arial 30 bold")
        temp.place(x=10,y=60+42*i)
        heart_labels.append(temp)
    while True:
        t1=time.time()
        for train in trains:
            game_area.move(train,0,px)
            if game_area.coords(train)[1]>105*py:
                trains.remove(train)
                game_area.delete(train)
        
        for coin in coins:
            game_area.move(coin,0,px)
            if game_area.coords(coin)[1]>105*py:
                coins.remove(coin)
                game_area.delete(coin)
                
        x,y=game_area.coords(pl)

        
        objs = game_area.find_overlapping(x,y,x+5,y+5)
        if len(objs)>1:
            for i in objs:
                if i in trains:
                    hp-=1
                    heart_labels[-1].destroy()
                    heart_labels.pop(hp)
                    trains.remove(i)
                    game_area.delete(i)
                    root.title(str(hp)+" | "+str(train_amount))
                    if hp==0:
                        coins.append(game_area.create_text(50*px,50*py,text="You lose!",fill = "red",font = "Arial 200 bold"))
                        need_break = True
                elif i in coins:
                    coin_amount+=1
                    coin_Label["text"]=str(coin_amount)
                    coins.remove(i)
                    game_area.delete(i)
                        
        if need_break:
            break
        
        game_area.update()
        t+=1
        if not t%15:
            create_coin()
        if not t%35:
            create_train()
            train_amount+=1
            root.title(str(hp)+" | "+str(train_amount))
            
        t2=time.time()
        z=1/(0.1*t+50)-(t2-t1)
        time.sleep(z*(z>0))

coins=[]
        
def create_train():
    xr=randint(0,2)*30*px+19*px
    trains.append(game_area.create_image(xr,2*px,image=train_image))        
        
def create_coin():
    xr=randint(0,2)*30*px+19*px
    coins.append(game_area.create_oval(xr,2*px,xr+2*px,2*px+2*px,fill="yellow"))

def move(event):
    if (event.keycode==37 and game_area.coords(pl)[0]>20*px):
      game_area.move(pl,-30*px,0)
    if (event.keycode==39 and game_area.coords(pl)[0]<80*px):
      game_area.move(pl,30*px,0)  
    
    
root=Tk()
root.state("zoomed")
width=root.winfo_vrootwidth()-100
height=root.winfo_vrootheight()
px=width/100
py=height/100
Button(root,text="RESTART",command=procces).place(x=101*px,y=10)
game_area=Canvas(root,width=root.winfo_vrootwidth()-100,height=root.winfo_vrootheight(),bg="white")
game_area.place(x=0,y=0)
pl_img=PhotoImage(file="pepe.png")
train_image = PhotoImage(file="train.png")
pl = game_area.create_image(50*px,85*py,image=pl_img)

root.bind("<Key>",move)
info_frame=Frame(root,width=100,height=50*py,bg="white")
info_frame.place(x=101*px,y=30)
procces()
root.mainloop()
