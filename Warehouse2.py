from tkinter import *
win = Tk()
win.title("Ware House")

toolbar = Frame(win, bg = "cyan")
insertButt=Button(toolbar,text="Insert Image", command=doNothing)
insertButt.pack(side = LEFT,padx=3,pady=3)
printButt=Button(toolbar,text="Print", command=doNothing)
printButt.pack(side = LEFT,padx=3,pady=3)
toolbar.pack(side=TOP,fill=X)

status =Label(win,text="test testing...", bd=2, relief=SUNKEN,anchor=W)
status.pack(side = BOTTOM,fill=X)

win.mainloop()
