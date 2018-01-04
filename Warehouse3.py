from tkinter import *
import tkinter.messagebox
win=Tk()
tkinter.messagebox.showinfo("Test 1")
answer=tkinter.messagebox.askquestion("test my answer")

if answer == 'yes':
    print("okay na okay")
win.mainloop()
