from tkinter import *
from os import system
def clear(frame):
    for slave in frame.place_slaves():
        slave.destroy()
def show_create_app():
    def create_app():
        global app_name
        app_name = app_ent.get()
        project.add_app(Application(prject,way,app_name))
    clear(begin_frame)
    Label(begin_frame, font="Arial 20 bold",
          text="Выберите название").place(x=0.4 * w, y=0.4 * h,
                                          width=0.2 * w, height=0.1 * h)
    app_ent = Entry(begin_frame)
    app_ent.place(x=0.4 * w, y=0.5 * h, width=0.2 * w, height=0.05 * h)
    Button(begin_frame, text="Создать", font="Arial 20 bold",
           command=create_app).place(x=0.4 * w, y=0.6 * h,
                                         width=0.2 * w, height=0.1 * h)

def show_create_project():
    def create_project():
        global way,pr_name,project
        way = way_ent.get()
        pr_name= name_ent.get()
        project=Project(way,pr_name)
        show_create_app()
        show_create_app()
    clear(begin_frame)
    Label(begin_frame,
          font = "Arial 20 bold",text="Выберите путь"
          ).place(x=0.4*w,y=0.1*h,width = 0.2*w, height=0.1*h)
    way_ent = Entry(begin_frame)
    way_ent.place(x=0.4*w,y=0.2*h,width = 0.2*w, height=0.05*h)
    Label(begin_frame,font = "Arial 20 bold",
          text="Выберите название").place(x=0.4 * w, y=0.4 * h,
                        width=0.2 * w, height=0.1 * h)
    name_ent = Entry(begin_frame)
    name_ent.place(x=0.4 * w, y=0.5 * h, width=0.2 * w, height=0.05 * h)
    Button(begin_frame, text="Создать", font="Arial 20 bold",
           command=create_project).place(x=0.4 * w, y=0.6 * h,
                   width=0.2 * w, height=0.1 * h)

root = Tk()
w = root.winfo_vrootwidth()
h = root.winfo_vrootheight()
root.title("Django Editor")
root.state("zoomed")

begin_frame = Frame(root, width=w, height=h)
begin_frame.place(x=0,y=0)
Button(begin_frame,font = "Arial 20 bold",text = "Создать проект",command = show_create_project).place(x=0.4*w,y=0.3*h,width = 0.2*w, height=0.1*h)
Button(begin_frame,font = "Arial 20 bold",text = "Открыть проект").place(x=0.4*w,y=0.41*h,width = 0.2*w, height=0.1*h)

root.mainloop()
