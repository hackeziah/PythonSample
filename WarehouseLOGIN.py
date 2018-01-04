from tkinter import *

win = Tk()
win.title("LOGIN FORM")

f1=Frame(win,width=500,height=50,bg="sky blue")
f1.grid(row=0,column=0)

f2=Frame(win,width=500,height=50,bg="sky blue")
label_1 = Label(f2, text="USERNAME : ",font=('arial',15,'bold'),bg="sky blue")
label_2 = Label(f2, text="PASSWORD : ",font=('arial',15,'bold'),bg="sky blue")

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

t1=StringVar()
text1=Entry(f2,textvariable=t1,bd=3)
text1.grid(row=0, column=1)
t2=StringVar()
text2=Entry(f2,textvariable=t1,bd=3)
text2.grid(row=1, column=1)
f2.grid(row=1,column=0)

f3=Frame(win,width=500,height=35,bg="sky blue")

lstbox=Listbox(f3,height=1)
sb=Scrollbar(f3,orient=VERTICAL)
sb.pack(side=RIGHT,fill=Y)
sb.configure(command=lstbox.yview)
lstbox.configure(yscrollcommand=sb.set)
lstbox.pack()
f3.grid(row=2,column=0)

f4=Frame(win,width=500,height=100,bg="sky blue")
logbtn = Button(f4, text="LOGIN",bg="cyan",width=9,height=1,font=('arial',15,'bold'))
logbtn.grid(row=0,column=0)

cancelbtn = Button(f4, text="CANCEL",bg="cyan",width=9,height=1,font=('arial',15,'bold'))
cancelbtn.grid(row=0,column=3)

f4.grid(row=3,column=0)


win.mainloop()
