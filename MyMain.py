import mysql.connector
from tkinter import *
from tkinter import ttk
import random
number= random.randint(0,9999)
number1= random.randint(0,6666)
win=Tk()
win.title("WAREHOUSE MANAGEMENT SYSTEM(ADD STOCK)")


f1=Frame(win,width=136,height=650,bg="sky blue")
l1 = Label(f1, text="PRODUCT ID",font=('arial',13,'bold'))
l1.grid(row = 0, column =0 )

l2 = Label(f1, text="PRODUCT NAME",font=('arial',13,'bold'))
l2.grid(row = 1, column = 0)

l3 = Label(f1, text="STOCK LEVEL",font=('arial',13,'bold'))
l3.grid(row = 2, column = 0)

l4 = Label(f1, text="VALUE OF PACKAGE:",font=('arial',13,'bold')) 
l4.grid(row = 3, column = 0)

l5 = Label(f1, text="COST PER UNIT:",font=('arial',13,'bold')) 
l5.grid(row = 4, column = 0)

t1=StringVar()
text1=Entry(f1,textvariable=t1,bd=3)
text1.grid(row = 0, column = 1)
t1.set(number)
t2=StringVar()
text2=Entry(f1,textvariable=t2,bd=3)
text2.grid(row = 1, column = 1)


t3 = StringVar()
box1 = ttk.Combobox(f1, textvariable=t3, state='readonly')
box1['values'] = ('FURNITURE','ELECTRONIC GADGETS','CONSUMABLES','SCHOOL SUPPLIES','PARTS')
box1.current(0)
box1.grid(row = 2, column = 1)

t4=StringVar()
text4=Entry(f1,textvariable=t4,bd=3)
text4.grid(row =3, column = 1)
t5=StringVar()

text5=Entry(f1,textvariable=t5,bd=3)
text5.grid(row = 4, column = 1)




l1 = Label(f1, text="ORDER ID",font=('arial',13,'bold'))
l1.grid(row = 0, column =2 )

l2 = Label(f1, text="CUSTOMER",font=('arial',13,'bold'))
l2.grid(row = 1, column = 2)

l3 = Label(f1, text="CONTACT:",font=('arial',13,'bold'))
l3.grid(row = 2, column = 2)

l4 = Label(f1, text="DATE TIME IN:",font=('arial',13,'bold')) 
l4.grid(row = 3, column = 2)

l5 = Label(f1, text="DATE TIME OUT:",font=('arial',13,'bold')) 
l5.grid(row = 4, column = 2)

t6=StringVar()
text6=Entry(f1,textvariable=t6,bd=3)
text6.grid(row = 0, column = 3)
t6.set(number1)

t7=StringVar()
text7=Entry(f1,textvariable=t7,bd=3)
text7.grid(row = 1, column = 3)

t8=StringVar()
text8=Entry(f1,textvariable=t8,bd=3)
text8.grid(row = 2, column = 3)

t9=StringVar()
text9=Entry(f1,textvariable=t9,bd=3)
text9.grid(row =3, column = 3)

t10=StringVar()
text10=Entry(f1,textvariable=t10,bd=3)
text10.grid(row = 4, column = 3)

f1.grid(row = 0, column = 0)


f4=Frame(win,width=999,height=999,bg="orange")
l1 = Label(f4, text="Amount:",font=('arial',13,'bold')) 
l1.grid(row = 0, column = 0)

t11=StringVar()
text11=Entry(f4,textvariable=t11,bd=3)
text11.grid(row = 0, column = 1)

f4.grid(row = 4, column = 0)



def compute():
    q4=t4.get()
    q5=t5.get()
    total=int(q4)*int(q5)
    
    t11.set(total)

def cancel():
    t4.set("")
    t5.set("")
    t11.set("")

    
#=========================



def addstock():
    q1=t1.get()
    q2=t2.get()
    q3=t3.get()
    q4=t4.get()
    q5=t5.get()
    q6=t6.get()
    q7=t7.get()
    q8=t8.get()
    q9=t9.get()
    q10=t10.get()
    q11=t11.get()
    conn = mysql.connector.connect(host='localhost',
                               database='warehouse',
                               user='root',
                               password='')

    x = conn.cursor()
    sql = "INSERT INTO stocks(`proid`, `prona`, `stol`, `disc`, `cpu`, `oi`, `cust`, `ons`, `ior`, `add`, `amount`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
            x.execute(sql,(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11))
           
            conn.commit()
    except:
            conn.rollback()
            print ("NO QUERY CONNECT")  

            conn.close()


f2=Frame(win,width=999,height=999,bg="orange")
ad=Button(f2,text="ADD STOCK",font=('Verdana',15,'bold'),command=addstock).grid(row = 0, column = 0)
up=Button(f2,text="COMPUTE",font=('Verdana',15,'bold'),command=compute).grid(row = 0, column = 1)
up=Button(f2,text="DELETE",font=('Verdana',15,'bold'),command=cancel).grid(row = 0, column = 2)

f2.grid(row = 5, column = 0)




win.mainloop()
input()
