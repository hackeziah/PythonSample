from tkinter import *
import tkinter.messagebox as tm
import os
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="USERNAME",font=('arial',15,'bold'))
        self.label_2 = Label(self, text="PASSWORD",font=('arial',15,'bold'))

        self.entry_1 = Entry(self,bd=9)
        self.entry_2 = Entry(self, show="*",bd=9)

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)



        self.logbtn = Button(self, text="LOGIN", command = self._login_btn_clickked,bg="cyan",width=9,height=1,font=('arial',15,'bold'))
        self.logbtn.grid(row=6, column=1)

        self.logbtn = Button(self, text="CANCEL",bg="cyan",width=9,height=1,font=('arial',15,'bold'))
        self.logbtn.grid(row=6, column=2)
        self.pack()

    def _login_btn_clickked(self):
     
        username = self.entry_1.get()
        password = self.entry_2.get()


        if username == "admin" and password == "admin":
           yo=Tk()
           def go():
               os.system("mainy.py")
               
           Button(yo, text ="continue",command=go).pack()
            
            
        else:
            tm.showerror("Login error", "Incorrect username")




win = Tk()
win.title("LOGIN" )
lf = LoginFrame(win)

win.mainloop()
input()
