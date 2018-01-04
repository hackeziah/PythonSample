from tkinter import *
import time
import os

win = Tk()
win.geometry("1350x300+0+0")
win.title("Ware House")

text_Input=StringVar ()
Tops=Frame(win,width=1350,height=50,bg="orange")
Tops.pack(side=TOP)
bb=Frame(win,width=1350,height=50,bg="orange")
bb.pack(side=BOTTOM)


lbInfo=Label(Tops,font=('arial',50,'bold'),text="Ware House Management System",fg="black",bd=2,bg="orange")
lbInfo.grid(row=0,column=0)



#my menubar

menu =Menu(win)
def doNothing():
    print("my test :D")
win.config(menu=menu)

subMenu=Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project",command=doNothing)
subMenu.add_command(label="New",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command = doNothing)

RepMenu=Menu(menu)
menu.add_cascade(label="Report", menu = RepMenu)

editMenu=Menu(menu)
menu.add_cascade(label="Edit", menu = editMenu)
editMenu.add_command(label="Redo",command=doNothing)

histMenu=Menu(menu)
menu.add_cascade(label="History", menu = histMenu)

HelMenu=Menu(menu)
menu.add_cascade(label="Help", menu = HelMenu)

def addstock():
    os.system("MyMain.py")
def addd():
    os.system("reg.py")
def info():
    os.system("userinfo.py")
def rep():
    os.system("report.py")
def rev():
    os.system("rev.py")
def canc():
    os.system("can.py")


    
ad=Button(bb,text="ADD STOCK",command=addstock,font=('arial',20,'bold')).grid(row =1, column = 0)
up=Button(bb,text="RECEIVING PACKAGE",command=rev,font=('arial',20,'bold')).grid(row =1, column = 1)
up=Button(bb,text="CANCEL TRANSACTION",command=canc,font=('arial',20,'bold')).grid(row =1, column = 2)
up=Button(bb,text="REPORT",command=rep,font=('arial',20,'bold')).grid(row = 1, column = 3)
up=Button(bb,text="EMPLOYEE INFORMATION",command=info,font=('arial',20,'bold')).grid(row = 1, column = 4)
up=Button(bb,text="ADD ACOOUNT",command=addd,font=('arial',20,'bold')).grid(row = 1, column = 5)







#toolbar = Frame(win, bg = "cyan")
#insertButt=Button(toolbar,text="Insert Image", command=doNothing)
#insertButt.pack(side = LEFT,padx=2,pady=2)
#printButt=Button(toolbar,text="Print", command=doNothing)
#printButt.pack(side = LEFT,padx=2,pady=2)
#toolbar.pack(side=TOP,fill=X)

status =Label(win,text="test testing...", bd=2, relief=SUNKEN,anchor=W)
status.pack(side = BOTTOM,fill=X)


win.mainloop()
input()
