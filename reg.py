import mysql.connector
from tkinter import *
win=Tk()
win.title("REGISTRATION")
f1=Frame(win,width=136,height=650,bg="sky blue")
l1 = Label(f1, text="NAME",font=('arial',13,'bold'))
l1.grid(row = 0, column =0 )


t1=StringVar()
text1=Entry(f1,textvariable=t1,bd=3)
text1.grid(row = 0, column = 2)

l2 = Label(f1, text="CONTACT NO.",font=('arial',13,'bold'))
l2.grid(row = 1, column = 0)
l3 = Label(f1, text="EMAIL ADDRESS",font=('arial',13,'bold'))
l3.grid(row = 2, column = 0)
l4 = Label(f1, text="USER NAME:",font=('arial',13,'bold')) 
l4.grid(row = 3, column = 0)
l5 = Label(f1, text="PASSWORD:",font=('arial',13,'bold')) 
l5.grid(row = 4, column = 0)


t2=StringVar()
text2=Entry(f1,textvariable=t2,bd=3)
text2.grid(row = 1, column = 2)

t3=StringVar()
text3=Entry(f1,textvariable=t3,bd=3)
text3.grid(row = 2, column = 2)

t4=StringVar()
text4=Entry(f1,textvariable=t4,bd=3)
text4.grid(row =3, column = 2)
t5=StringVar()

text5=Entry(f1,textvariable=t5,bd=3,show="*")
text5.grid(row = 4, column = 2)


f1.grid(row = 1, column = 0)

f2=Frame(win,width=1350,height=50,bg="orange")



f2.grid(row = 2, column = 0)




def regis():
    q1=t1.get()
    q2=t2.get()
    q3=t3.get()
    q4=t4.get()
    q5=t5.get()
    conn = mysql.connector.connect(host='localhost',
                               database='warehouse',
                               user='root',
                               password='')

    x = conn.cursor()
    sql = "INSERT INTO register(name,contact,email,user,pass) VALUES (%s,%s,%s,%s,%s)"
    try:
            x.execute(sql,(q1,q2,q3,q4,q5))
           
            conn.commit()
    except:
            conn.rollback()
            print ("NO")  

            conn.close()
ad=Button(f2,text="REGISTER",command=regis,font=('arial',12,'bold')).grid(row = 0, column = 0)
up=Button(f2,text="CANCEL",font=('arial',12,'bold')).grid(row = 0, column = 1)


win.mainloop()
input()
