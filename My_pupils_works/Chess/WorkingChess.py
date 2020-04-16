from tkinter import*
from logic_chess import check
active_figure = ""
active_x=0
active_y=0
last_move = 9820
fr=0
to=0
#0-black
#1-white
def click(event):
    global active_figure,last_move,active_x,active_y,fr,to
    if (event.widget["text"] and not active_figure):
        if ((last_move>9817 and ord(event.widget["text"])<9818) or
            (last_move<9818 and ord(event.widget["text"])>9817)):
            active_figure=event.widget["text"]
            fr=event.widget
            active_x=event.widget.x
            active_y=event.widget.y
            last_move=ord(active_figure)
            #event.widget["text"]=""
            event.widget["fg"] = "green"
    elif ((not event.widget["text"]) or
          ((ord(event.widget["text"])>9817 and last_move<9818) or
          (ord(event.widget["text"])<9818 and last_move>9817) and event.widget["text"])):
        to=event.widget
        print("!")
        if check(deck_but,fr,to):
            event.widget["text"]=active_figure
            active_figure=""
            for i in root.place_slaves():
                if i["fg"]=="green":
                    i["text"]=""
                    i["fg"]="black"
    
        
#black>=9818
#white<=9817
deck = [
[chr(9820),chr(9822),chr(9821),chr(9818),chr(9819),chr(9821),chr(9822),chr(9820)],
[chr(9823)for i in range(8)],
["" for i in range (8)],
["" for i in range (8)],
["" for i in range (8)],
["" for i in range (8)],
[chr(9817) for i in range(8)],
[chr(9814),chr(9816),chr(9815),chr(9813),chr(9812),chr(9815),chr(9816),chr(9814)]
]
deck_but=[[0 for i in range(8)] for i in range(8)]
root=Tk()
root.state("zoomed")
size=40
colors=["#ffffff","#777777"]
for y in range(8):
     for x in range(8):
         t=Button(root, text = deck[y][x],font="Arial 20",bg=colors[(x+y)%2])
         t.x=x
         t.y=y
         t.bind("<1>",click)
         t.place(x=10+size*x,y=10+size*y,width=size,height=size)
         deck_but[y][x] = t

root.mainloop()

