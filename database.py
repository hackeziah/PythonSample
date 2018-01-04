from tkinter import *
win=Tk()
win.title("PHONE RECORD")
f1=Frame(win)
l1 = Label(f1, text="NAME")
l1.grid(row = 0, column =0 )


t1=StringVar()
text1=Entry(f1,textvariable=t1,bd=3)
text1.grid(row = 0, column = 2)

l2 = Label(f1, text="PHONE")
l2.grid(row = 1, column = 0)


t2=StringVar()
text2=Entry(f1,textvariable=t2,bd=3)
text2.grid(row = 1, column = 2)
f1.grid(row = 1, column = 0)

f2=Frame(win)

ad=Button(f2,text="ADD").grid(row = 0, column = 0)
up=Button(f2,text="UPDATE").grid(row = 0, column = 1)
de=Button(f2,text="DELETE").grid(row = 0, column = 2)
lo=Button(f2,text="LOAD").grid(row = 0, column = 3)
f2.grid(row = 2, column = 0)


f3=Frame(win)
lstbox=Listbox(f3,height=10)
sb=Scrollbar(f3,orient=VERTICAL)
sb.pack(side=RIGHT,fill=Y)
sb.configure(command=lstbox.yview)
lstbox.configure(yscrollcommand=sb.set)
lstbox.pack()
f3.grid(row = 3, column = 0)
win.mainloop()

