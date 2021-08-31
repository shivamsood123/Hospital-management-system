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

def remove():
    global e3,edd
    edd=e3.get(tkinter.ACTIVE)
    mycursor.execute("select * from appointment where AP_NO=%s", (edd,))
    v=mycursor.fetchone()
    if (v==None):
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "PATIENT APPOINTMENT NOT FIXED")
    else:
        mycursor.execute("DELETE FROM APPOINTMENT where AP_NO=%s",(edd,))
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "PATIENT APPOINTMENT DELETED")
        mydb.commit()

rootAP=None

def viewappointment():
    global e8,rootAP
    ap=str(e8.get())
    mycursor.execute("select * from appointment where AP_DATE=%s", (ap,))
    vv=mycursor.fetchall()
    
    if vv==None:
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "NO APPOINTMENT FOR TODAY")
    else:
        mycursor.execute("Select * from appointment where AP_DATE=%s",(ap,))
        s=mycursor.fetchall()
    
        counter=150
        for i in s:
            t=tkinter.Label(rootAP,text=i,bg='white',fg='cyan4',width=42,font='Arial 12',height=2)
            t.place(x=50,y=counter)
            counter+=50
            
def va():
    global rootAP,e8
    rootAP=tkinter.Tk()
    rootAP.geometry("500x500")
    rootAP.configure(background='cyan4')
    rootAP.title("TODAYS APPOINTMENTS")

    head3=tkinter.Label(rootAP,text="VIEW APPOINTMENTS",bg='white',fg='cyan4',font="Times 16 bold italic",height=1)
    head3.place(x=0,y=0)
    h1=tkinter.Label(rootAP,text="ENTER DATE :",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    h1.place(x=50,y=50)
    e8=tkinter.Entry(rootAP,bg='white',fg='cyan4',width=20,font='Arial 12')
    e8.place(x=250,y=50)
    b5=tkinter.Button(rootAP,text="SEARCH",command=viewappointment,font="arial 12",bg='gray25',fg='cyan4',height=1,width=42)
    b5.place(x=50,y=100)
    rootAP.mainloop()

rootAA=None

def sett():
    global e3,e1,e2,e4,e5,e6,mycursor,mydb
    p1=e1.get()
    p2=e2.get()
    p3=e3.get(tkinter.ACTIVE)
    p4=e4.get()
    p5=e5.get()
    p6=e6.get(1.0,tkinter.END)
    mycursor.execute("Insert into appointment values(%s,%s,%s,%s,%s,%s)",(p1,p2,p3,p4,p5,p6,))
    mydb.commit()
    tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "APPOINTMENT SET SUCCSESSFULLY")


def appo():
    global rootAA,L,e1,e2,e3,e4,e5,e6
    rootAA=tkinter.Tk()
    rootAA.geometry("500x550")
    rootAA.configure(background='cyan4')
    rootAA.title("APPOINTMENTS")
    
    H=tkinter.Label(rootAA,text="APOINTMENTS BOOKING",bg='white',fg='cyan4',font="Times 16 bold italic",height=1)
    H.place(x=0,y=0)
    l1=tkinter.Label(rootAA,text="PATIENT ID",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    l1.place(x=50,y=50)
    e1=tkinter.Entry(rootAA,bg='white',fg='cyan4',width=20,font='Arial 12')
    e1.place(x=250,y=50)
    l2 = tkinter.Label(rootAA,text="DOCTOR ID",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    l2.place(x=50,y=100)
    e2 = tkinter.Entry(rootAA,bg='white',fg='cyan4',width=20,font='Arial 12')
    e2.place(x=250, y=100)
    l3 = tkinter.Label(rootAA,text="APPOINTMENT NO",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    l3.place(x=50,y=150)
    L=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50']
    e3=tkinter.Listbox(rootAA,bg='white',fg='cyan4',width=20,font='Arial 12', height=1, selectmode='SINGLE', exportselection=0)
    for jjj in L:
        e3.insert(tkinter.END, jjj)
    e3.place(x=250,y=150)
    l4 = tkinter.Label(rootAA,text="TIME(HH:MM:SS)",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    l4.place(x=50,y=200)
    e4=tkinter.Entry(rootAA,bg='white',fg='cyan4',width=20,font='Arial 12')
    e4.place(x=250,y=200)
    l5 = tkinter.Label(rootAA,text="DATE(YYYY-MM-DD)",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    l5.place(x=50,y=250)
    e5=tkinter.Entry(rootAA,bg='white',fg='cyan4',width=20,font='Arial 12')
    e5.place(x=250,y=250)
    l6=tkinter.Label(rootAA,text="DESCRIPTION",bg='gray25',fg='white',height=1,width=40,font='Arial 12')
    l6.place(x=50,y=300)
    e6=tkinter.Text(rootAA,bg='white',fg='cyan4',width=40,font='Arial 12',height=3)
    e6.place(x=50,y=330)
    
    b1=tkinter.Button(rootAA,text="SUBMIT",command=sett,font="arial 12",bg='gray25',fg='cyan4',height=1,width=10)
    b1.place(x=50,y=400)
    b2=tkinter.Button(rootAA,text="DELETE",command=remove,font="arial 12",bg='gray25',fg='cyan4',height=1,width=10)
    b2.place(x=150,y=400)
    b4=tkinter.Button(rootAA,text="TODAYS APPOINTMENTS",command=va,font="arial 12",bg='gray25',fg='cyan4',height=1)
    b4.place(x=250,y=400)
    rootAA.mainloop()


