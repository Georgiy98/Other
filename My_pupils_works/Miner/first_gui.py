from tkinter import *
from random import randint,shuffle
from time import sleep
def mark(event):
    global flags,game_status
    if game_status == "active":
        if event.widget.status=="hidden":
            if event.widget["image"]=="":
                if flags>0:
                    flags-=1
                    flag_amount_label["text"]=":"+str(flags)
                    event.widget["image"]=flag
            else:
                flags+=1
                flag_amount_label["text"]=":"+str(flags)
                event.widget["image"]=""
def check(event):
    global game_status
    if game_status == "active":
        if event.widget["image"]=="":
            event.widget.status="opened"
            if event.widget.value=="mine":
                game_status="loose"
                event.widget["image"]=mine
                for line in buts:
                    for but in line:
                        if but.value == "mine":
                            but["image"]=mine
                root.update()
                sleep(3)
                end_game("You loose!")
            else:
                event.widget["relief"] = "flat"
                event.widget["bd"] = 0
                num=count_mines(event.widget.x,event.widget.y)
                event.widget["text"]=str(num)
                if num == 0:
                    show(event.widget.x,event.widget.y)
                if check_win():
                    sleep(1)
                    end_game("You won!")
def get_near(x,y):
    res=[]
    for xi in range(max(x-1,0),min(x+2,w)):
        for yi in range(max(y-1,0),min(y+2,h)):
            res.append(buts[xi][yi])
    res.remove(buts[x][y])
    return res

def end_game(res):
    result_label["text"]=res
    field.place(x=-2000,y=0)
    end_frame.place(x=10,y=10)

def check_win():
    global w,h,level
    res = 0
    for but in field.place_slaves():
        if but.status == "opened":
            res+=1
    return res == w*h-int(level*w*h)
def count_mines(x,y):
    res=0
    for but in get_near(x,y):
        if but.value == "mine":
            res+=1
    return res

def show(x,y):
    zeroes=[]
    for but in get_near(x,y):
        num = count_mines(but.x,but.y)
        but["relief"] = "flat"
        but["bd"] = 0
        but["text"]=str(num)
        if (num == 0 and but.status=="hidden"):
            zeroes.append(but) 
        but.status= "opened"
    for but in zeroes:
        show(but.x, but.y)
        
def restart():
    global w,h,flags,level,game_status,buts
    h=randint(5,10)
    w=randint(10,20)
    for but in field.place_slaves():
        but.destroy()
    field.place(x=0,y=50,width=b*w+10,height = b*h+10)
    end_frame.place(x=-2000,y=0)
    buts=[]
    for x in range(w):
        buts.append([])
        for y in range(h):
            t=Button(field,bd=4)
            t.value = "free"
            t.status = "hidden"
            t.x=x
            t.y=y
            t.place(x=x*b,y=y*b,width=b,height=b)
            t.bind("<3>",mark)
            t.bind("<1>",check)
            buts[-1].append(t)
    temp_list = field.place_slaves()       
    shuffle(temp_list)
    flags = int(level*w*h)
    temp_list=temp_list[:flags]
    game_status = "active"
    level=0.15
    flag_amount_label["text"]=":"+str(flags)
    for but in temp_list:
        but.value = "mine"
root = Tk()
root.title("Saper")
root.state("zoomed")

flag = PhotoImage(file = "flag.png")
mine = PhotoImage(file = "mine.png")

game_status = "active"
field = Frame(root,bd=5,bg="brown")
b=34
h=randint(5,10)
w=randint(10,20)
level=0.15
Label(root, image = flag).place(x=10,y=10)
flags = int(level*w*h)
flag_amount_label = Label(root,text=":"+str(flags),font = "Arial 18")
flag_amount_label.place(x=40,y=10)

end_frame = Frame(root,width = 200,height=300, bg="#dddddd")
result_label = Label(end_frame, font = "Arial 30", text = "Try it..")
result_label.place(x=0,y=10,width=200,height=50)
Button(end_frame, font="Arial 80 bold", text=chr(8634), command=restart).place(x=60,y=200,width=80,height=80)
restart()
root.mainloop()
