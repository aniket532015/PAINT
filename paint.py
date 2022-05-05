from tkinter import*
dsc=Tk()
dsc.geometry("720x480")
dsc.title("Paint Application")
dsc.configure(bg="violet")
lal=Label(dsc,text="Draw").pack()
giet=Canvas(dsc,width=720,height=480,bg="white")
giet.pack()

def redc():
    global color
    color="red"
    giet.bind('<B1-Motion>',paint_page)
def yellowc():
    global color
    color="yellow"
    giet.bind('<B1-Motion>',paint_page)
def bluec():
    global color
    color="blue"
    giet.bind('<B1-Motion>',paint_page)
def greenc():
    global color
    color="green"
    giet.bind('<B1-Motion>',paint_page)

btn=Button(dsc,text="red colour",bg="red",fg="white",command=redc)
btn.place(x=20,y=30)
btn=Button(dsc,text="yellow colour",bg="yellow",fg="white",command=yellowc)
btn.place(x=20,y=60)
btn=Button(dsc,text="blue colour",bg="blue",fg="white",command=bluec)
btn.place(x=20,y=90)
btn=Button(dsc,text="green colour",bg="green",fg="white",command=greenc)
btn.place(x=20,y=120)


def paint_page(event):
    x1,y1=(event.x-3),(event.y-3)
    x2,y2=(event.x+3),(event.y+3)
    giet.create_oval(x1,y1,x2,y2,fill=color,outline=color)
dsc.mainloop()
