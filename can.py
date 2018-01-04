from tkinter import *
import time
win = Tk()
f1=Frame(win,width=700,height=50,bg="black")
l1=Label(win,font=('arial',50,'bold'),text="CANCEL TRANSACTION",fg="sky blue",bd=1)
l1.grid(row=0,column=0)
f1.grid(row=0,column=0)
f2=Frame(win,width=700,height=500,bg="orange")
f2in=Frame(win,width=650,height=450,bg="pink")
f2in.grid(row=1,column=0)
f2.grid(row=1,column=0)
win.mainloop()
input()
