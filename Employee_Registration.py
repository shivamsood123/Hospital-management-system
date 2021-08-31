import tkinter
from tkinter import messagebox

import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sood@123',
    database='HOSPITAL'
	)
mycursor = mydb.cursor()

rootE=None
var=None

def delo():
    global d1,de
    de=str(t1.get())
    mycursor.execute("select * from employee where EMP_ID=%s", (de,))
    p=mycursor.fetchone()
    
    if (p!=None):
        mycursor.execute("DELETE from employee where EMP_ID=%s", (de,))
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE RECORD DELETED")
        mydb.commit()
    else:
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DOESN'T EXIST")

def inp():
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,var, mycursor, mydb
    e1=t1.get()
    e2=t2.get()
    e3=str(var.get())
    e4=t3.get()
    e5=lb.get(tkinter.ACTIVE)
    e6=t4.get()
    e7=t5.get()
    e8=t6.get()
    e9=t7.get()
    mycursor.execute("INSERT INTO employee VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(e1,e2,e3,e4,e5,e6,e7,e8,e9,))
    mydb.commit()
    tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA ADDED")

def ex():
    rootE.destroy()

def emp_screen():
    global rootE,t1,t2,r1,r2,t3,lb,t4,t5,t6,t7,var
    rootE=tkinter.Tk()
    rootE.title("EMPLOYEE REGISTRATION")
    rootE.geometry('500x800')
    rootE.configure(background='cyan4')
    
    H=tkinter.Label(rootE,text="EMPLOYEE REGISTRATION",bg='white',fg='cyan4',font="Times 16 bold italic",height=1)
    H.place(x=0,y=0)
    l1=tkinter.Label(rootE,text="EMPLOYEE ID",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    l1.place(x=50,y=50)
    t1=tkinter.Entry(rootE,bg='white',fg='cyan4',width=20,font='Arial 12')
    t1.place(x=250,y=50)
    l2 = tkinter.Label(rootE, text="EMPLOYEE NAME",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    l2.place(x=50,y=100)
    t2 = tkinter.Entry(rootE,bg='white',fg='cyan4',width=20,font='Arial 12')
    t2.place(x=250, y=100)
    l3 = tkinter.Label(rootE, text="SEX",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    l3.place(x=50,y=150)
    var = tkinter.StringVar(master=rootE)
    r1 = tkinter.Radiobutton(rootE, text="MALE", variable=var, value="Male",bg='white',fg='cyan4',font='Arial 12')
    r1.place(x=250, y=150)
    r2 = tkinter.Radiobutton(rootE, text="FEMALE", variable=var, value="Female",bg='white',fg='cyan4',font='Arial 12')
    r2.place(x=325, y=150)
    l4 = tkinter.Label(rootE, text="AGE",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    l4.place(x=50,y=200)
    t3=tkinter.Entry(rootE,bg='white',fg='cyan4',width=20,font='Arial 12')
    t3.place(x=250,y=200)
    l5 = tkinter.Label(rootE, text="EMPLOYEE TYPE",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    l5.place(x=50,y=250)
    lb = tkinter.Listbox(rootE, selectmode='SINGLE', exportselection=0, height=1,bg='white',fg='cyan4',width=20,font='Arial 12')
    lb.insert(tkinter.END, "DOCTOR")
    lb.insert(tkinter.END, "NURSE")
    lb.insert(tkinter.END, "RECEPTIONIST")
    lb.place(x=250, y=250)
    l6=tkinter.Label(rootE,text="SALARY",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    l6.place(x=50,y=300)
    t4=tkinter.Entry(rootE,bg='white',fg='cyan4',width=20,font='Arial 12')
    t4.place(x=250,y=300)
    l7 = tkinter.Label(rootE, text="EXPERIENCE",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    l7.place(x=50,y=350)
    t5 = tkinter.Entry(rootE,bg='white',fg='cyan4',width=20,font='Arial 12')
    t5.place(x=250,y=350)
    l8 = tkinter.Label(rootE, text="MOBILE NO",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    l8.place(x=50,y=400)
    t7 = tkinter.Entry(rootE,bg='white',fg='cyan4',width=20,font='Arial 12')
    t7.place(x=250,y=400)
    l9 = tkinter.Label(rootE, text="EMAIL",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    l9.place(x=50,y=450)
    t6=tkinter.Entry(rootE,bg='white',fg='cyan4',width=20,font='Arial 12')
    t6.place(x=250,y=450)
    b1=tkinter.Button(rootE,text="SUBMIT",command=inp,font="arial 12",bg='gray25',fg='cyan4',height=1,width=10)
    b1.place(x=50,y=500)
    b2=tkinter.Button(rootE,text="DELETE",command=delo,font="arial 12",bg='gray25',fg='cyan4',height=1,width=10)
    b2.place(x=150,y=500)
    b3=tkinter.Button(rootE,text="EXIT",command=ex,font="arial 12",bg='gray25',fg='cyan4',height=1,width=10)
    b3.place(x=250,y=500)
    rootE.mainloop()


