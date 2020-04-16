import winsound
import tkinter as tk
import os

message = "Nice to meet you"

def say(message,vol):
    with open("here.vbs","w") as f:
        f.write("""
        Dim speaks, speech 
    speaks="%s" 
    Set speech=CreateObject("sapi.spvoice") 
    speech.Speak speaks 
    with speech 
    .Volume = 100 
    .Rate = %s
    end with 
    """%(message,vol))
    os.system("here.vbs")
    os.remove("here.vbs")
say(message,80)

def play(event):
    for i in event.widget.mus:
        winsound.Beep(i[0],i[1])
star_wars = [(440,500),(440,500),(440,500),(349,350),(523,150),(440,500) ,(349,350) ,(523,150) ,(440,1000) ,(659,500) ,(659,500) ,(659,500) ,(698,350) ,(523,150) ,(415,500) ,(349,350) ,(523,150) ,(440,1000)]
mission_impossible = [(784,150) ,(784,150),(932,150)  ,(1047,150)  ,(784,150)  ,(784,150) ,(699,150)  ,(740,150)  ,(784,150)  ,(784,150)  ,(932,150)  ,(1047,150)  ,(784,150)  ,(784,150)  ,(699,150)  ,(740,150) ,(932,150)  ,(784,150)  ,(587,1200)  ,(932,150)  ,(784,150)  ,(554,1200)  ,(932,150)  ,(784,150)  ,(523,1200)  ,(466,150)  ,(523,150)]
mario = [(659,250),(659,250),(659,300),(523,250),(659,250),(784,300),(392,300),(523,275),(392,275) ,(330,275) ,(440,250) ,(494,250) ,(466,275) ,(440,275) ,(392,275),(659,250),(784,250),(880,275),(698,275),(784,225),(659,250),(523,250),(587,225),(494,225)]
pine = [(247, 500),    (417, 500),    (417, 500),    (370, 500),    (417, 500),    (329, 500),    (247, 500),    (247, 500),    (247, 500),    (417, 500),    (417, 500),    (370, 500),    (417, 500),    (497, 500),   (37,500),    (497, 500),    (277, 500),    (277, 500),    (440, 500),    (440, 500),    (417, 500),    (370, 500),    (329, 500),    (247, 500),    (417, 500),    (417, 500),    (370, 500),    (417, 500),    (329, 500)]
texts = ["Star wars","Mission impossible","Mario","Pine"]
musics=[star_wars,mission_impossible,mario,pine]
root = tk.Tk()
root.title("Hello:)")
root.resizable(width=False, height=False)
root.geometry("220x220+500+200")
for i in range(4):
    t=tk.Button(root,font="Arial 12 bold",bg="#000000",fg="#ffff00", text=texts[i],cursor = "spider")
    t.place(x=10,y=10+50*i,width=200,height=40)
    t.mus = musics[i]
    t.bind("<1>",play)

root.mainloop()
