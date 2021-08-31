import tkinter
import tkinter.messagebox

import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sood@123',
    database='HOSPITAL'
	)
mycursor = mydb.cursor()

#variables
rootB=None

def date_up():
    global b1,b2
    b1 = P_id.get()
    b2 = dd.get()
    mycursor.execute("SELECT * FROM ROOM WHERE PATIENT_ID=%s",(b1,))
    p=mycursor.fetchone()

    if(p==None):
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "PATIENT ID NOT FOUND")
    else:
        mycursor.execute("UPDATE ROOM SET DATE_DISCHARGED=%s where PATIENT_ID=%s", (b2, b1,))
        mydb.commit()
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DISCHARGE DATE UPDATED")

def up():
    global c1, b1, P_id, b3, b4, b5, b6, dd, treat_1, treat_2, cost_t, b7, b8, med, med_q, price, u
    b1 = P_id.get()
    b3 = treat_1.get(tkinter.ACTIVE)
    b4 = treat_2.get(tkinter.ACTIVE)
    b5 = cost_t.get()
    b6 = med.get(tkinter.ACTIVE)
    b7 = med_q.get(tkinter.ACTIVE)
    b8 = price.get()
    mycursor.execute("INSERT INTO TREATMENT VALUES(%s,%s,%s,%s)", (b1, b3, b4, b5,))
    mycursor.execute("INSERT INTO MEDICINE VALUES(%s,%s,%s,%s)", (b1, b6, b7, b8,))
    mydb.commit()
    tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "BILLING DATA SAVED")

def calci():
    global b1
    b1 = P_id.get()
    mycursor.execute("Select sum(T_COST+ (M_COST*M_QTY) +(DATE_DISCHARGED-DATE_ADMITTED)*RATE) FROM ROOM r,TREATMENT t,MEDICINE m where r.PATIENT_ID=t.PATIENT_ID and t.PATIENT_ID=m.PATIENT_ID and m.PATIENT_ID=%s",(b1,) )
    u =mycursor.fetchone()
    tkinter.messagebox.showinfo("HOSPITL MANAGEMENT SYSTEM","TOTAL AMOUNT OUTSTANDING :"+str(u[0]))
    
L1=None
L2=None
L3=None
L4=None

def exitt():
    rootB.destroy()

def BILLING():
    global rootB,L1,treat1,P_id,dd,cost,med,med_q,price,treat_1,treat_2,cost_t,j,jj,jjj,jjjj,L2,L3,L4
    rootB=tkinter.Tk()
    rootB.geometry("500x700")
    rootB.configure(background='cyan4')
    rootB.title("BILLING SYSTEM")
    
    head=tkinter.Label(rootB,text="PATIENT BILL",bg='white',fg='cyan4',font="Times 16 bold italic",height=1)
    head.place(x=0,y=0)
    id = tkinter.Label(rootB, text="PATIENT ID",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    id.place(x=50, y=50)
    P_id = tkinter.Entry(rootB,bg='white',fg='cyan4',width=20,font='Arial 12')
    P_id.place(x=250, y=50)
    dd_l = tkinter.Label(rootB, text="DATE DISCHARGED",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    dd_l.place(x=50, y=100)
    dd = tkinter.Entry(rootB,bg='white',fg='cyan4',width=20,font='Arial 12')
    dd.place(x=250, y=100)
    ddp=tkinter.Button(rootB,text="UPDATE DISCHARGE DATE",command=date_up,font="arial 12",bg='gray25',fg='cyan4',height=1,width=40)
    ddp.place(x=50,y=150)
    treat = tkinter.Label(rootB, text="SELECT TREATMENT",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    treat.place(x=50, y=200)
    L1 = ["CONSULATION","SURGERY","LAB TEST"]
    treat_1= tkinter.Listbox(rootB,bg='white',fg='cyan4',width=20,font='Arial 12', height=1, selectmode='SINGLE', exportselection=0)
    for j in L1:
        treat_1.insert(tkinter.END, j)
    treat_1.place(x=250,y=200)
    treat_c = tkinter.Label(rootB, text="CODE",bg='gray25',fg='white',width=20,font='Arial 12',height=1)
    treat_c.place(x=50, y=250)
    L2 = ["C_1", "S_1", "L_1"]
    treat_2 = tkinter.Listbox(rootB,bg='white',fg='cyan4',width=20,font='Arial 12', height=1, selectmode='SINGLE', exportselection=0)
    for jj in L2:
        treat_2.insert(tkinter.END, jj)
    treat_2.place(x=250, y=250)
    costl= tkinter.Label(rootB, text="TREATMENT COST ₹",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    costl.place(x=50, y=300)
    cost_t = tkinter.Entry(rootB,bg='white',fg='cyan4',width=20,font='Arial 12')
    cost_t.place(x=250, y=300)
    med1 = tkinter.Label(rootB, text="SELECT MEDICINE",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    med1.place(x=50, y=350)
    L3 = ["NEURAL", "FANEKPLUS", "DISPRIN","DOLO+","BANDAGE","DIGENE"]
    med = tkinter.Listbox(rootB,bg='white',fg='cyan4',width=20,font='Arial 12', height=1, selectmode='SINGLE', exportselection=0)
    for jjj in L3:
        med.insert(tkinter.END, jjj)
    med.place(x=250, y=350)
    med_ql = tkinter.Label(rootB, text="QUANTITY",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    med_ql.place(x=50, y=400)
    L4 = [1,2,3,4,5,6,7,8,9,10]
    med_q = tkinter.Listbox(rootB,bg='white',fg='cyan4',width=20,font='Arial 12', height=1, selectmode='SINGLE', exportselection=0)
    for jjjj in L4:
        med_q.insert(tkinter.END, jjjj)
    med_q.place(x=250, y=400)
    pricel = tkinter.Label(rootB, text="MEDICINE PRICE ₹",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    pricel.place(x=50, y=450)
    price = tkinter.Entry(rootB,bg='white',fg='cyan4',width=20,font='Arial 12')
    price.place(x=250, y=450)
    b1=tkinter.Button(rootB,text="GENERATE BILL",command=calci,font="arial 12",bg='gray25',fg='cyan4',height=1,width=15)
    b1.place(x=50,y=500)
    b2 = tkinter.Button(rootB, text="REGISTER DATA", command=up,font="arial 12",bg='gray25',fg='cyan4',height=1,width=15)
    b2.place(x=200, y=500)
    ee=tkinter.Button(rootB,text="EXIT",command=exitt,font="arial 12",bg='gray25',fg='cyan4',height=1,width=10)
    ee.place(x=350,y=500)
    rootB.mainloop()

