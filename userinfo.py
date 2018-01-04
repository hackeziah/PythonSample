from tkinter import *
import time
win = Tk()
f1=Frame(win,width=700,height=50,bg="black")
l1=Label(win,font=('arial',50,'bold'),text="Users Information",fg="sky blue",bd=1)
l1.grid(row=0,column=0)
f1.grid(row=0,column=0)

f2=Frame(win,width=700,height=520,bg="orange")



fd2=Frame(f2,width=325,height=240,bg="red")
l1=Label(fd2,font=('arial',12,'bold'),text="User Name",fg="steel blue",bd=10, anchor='w')
l1.grid(row=0,column=0)

fd2.grid(row=0,column=0)



fd3=Frame(f2,width=325,height=240,bg="black")

fd3.grid(row=0,column=1)



f2.grid(row=1,column=0)


win.mainloop()
input()
