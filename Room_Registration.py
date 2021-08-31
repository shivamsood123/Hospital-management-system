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

P_id=None
rootR=None

##ROOM BUTTON
def room_button():
    global P_id,r1,r2,room_t,da,dd,rate,room_no,r3,r4,r5,r6,mycursor,mydb
    r1=P_id.get()
    r2=room_t.get(tkinter.ACTIVE)
    r3=room_no.get(tkinter.ACTIVE)
    r4=rate.get()
    r5=da.get()
    r6=dd.get()
    t=(r1,r3, r2, r4, r5, r6,)
    mycursor.execute("INSERT INTO ROOM VALUES(%s,%s,%s,%s,%s,%s)",t)
    tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "ROOM ALLOCATED")
    mydb.commit()
    
def update_button():
    global P_id,r1,r2,room_t,da,dd,rate,room_no,r3,r4,r5,r6,mycursor,mydb
    r1=P_id.get()
    r2=room_t.get(tkinter.ACTIVE)
    r3=room_no.get(tkinter.ACTIVE)
    r4=rate.get()
    r5=da.get()
    r6=dd.get()
    mycursor.execute("Select * from ROOM where PATIENT_ID=%s", (r1,))
    t = mycursor.fetchone()

    if t!=None:
        mycursor.execute("UPDATE ROOM SET ROOM_NO=%s,ROOM_TYPE=%s,RATE=%s,DATE_ADMITTED=%s,DATE_DISCHARGED=%s where PATIENT_ID=%s",(r3, r2, r4, r5, r6,r1,))
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "ROOM DETAILS UPDATED")
        mydb.commit()
    else:
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "PATIENT IS NOT ALLOCATED A ROOM")
        
##ROOT FOR DISPLAY ROOM INFO
rootRD=None

##EXIT FOR ROOM_PAGE
def EXITT():
    global rootR
    rootR.destroy()

##FUNCTION FOR ROOM DISPLAY
def R_search():
    global mycursor,P_id
    r1=P_id.get()
    mycursor.execute("select * from  ROOM  where PATIENT_ID=%s",(r1,))
    t = mycursor.fetchone()

    if (t==None):
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM","PATIENT NOT ALLOCATED ROOM")
    else:
        mycursor.execute("SELECT * FROM ROOM where PATIENT_ID=%s",(r1,))
        t = mycursor.fetchone()

        rootR1=tkinter.Tk()
        rootR1.title("ROOM DETAILS")
        rootR1.geometry("500x400")
        rootR1.configure(background='cyan4')
        
        r_head1=tkinter.Label(rootR1,text="ROOM DETAILS",bg='white',fg='cyan4',font="Times 16 bold italic",height=1)
        r_head1.place(x=0,y=0)
        id1=tkinter.Label(rootR1,text="PATIENT ID",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
        id1.place(x=50,y=50)
        P_id1=tkinter.Entry(rootR1,fg='cyan4',width=20,font='Arial 12')
        P_id1.insert(0,t[0])
        P_id1.place(x=250,y=50)
        room_tlab=tkinter.Label(rootR1,text="ROOM TYPE",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
        room_tlab.place(x=50, y=100)
        room_t1= tkinter.Entry(rootR1,fg='cyan4',width=20,font='Arial 12')
        room_t1.insert(0,t[1])
        room_t1.place(x=250,y=100)
        room_nolab=tkinter.Label(rootR1,text="ROOM NUMBER",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
        room_nolab.place(x=50,y=150)
        room_no1 = tkinter.Entry(rootR1,fg='cyan4',width=20,font='Arial 12')
        room_no1.insert(0,t[2])
        room_no1.place(x=250,y=150)
        ratel1=tkinter.Label(rootR1, text="ROOM CHARGES",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
        ratel1.place(x=50, y=200)
        rate1=tkinter.Entry(rootR1,fg='cyan4',width=20,font='Arial 12')
        rate1.insert(0,t[3])
        rate1.place(x=250, y=200)
        da_l1 = tkinter.Label(rootR1, text="DATE ADMITTED",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
        da_l1.place(x=50,y=250)
        da1=tkinter.Entry(rootR1,fg='cyan4',width=20,font='Arial 12')
        da1.insert(0,t[4])
        da1.place(x=250,y=250)
        dd_l1 = tkinter.Label(rootR1, text="DATE DISCHARGED",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
        dd_l1.place(x=50, y=300)
        dd1 =tkinter.Entry(rootR1,fg='cyan4',width=20,font='Arial 12')
        dd1.insert(0,t[5])
        dd1.place(x=250, y=300)
        rootR1.mainloop()

def exitt():
    rootR.destroy()

L=None
L1=None
def Room_all():
    global rootR,r_head,P_id,id,room_tl,L,i,room_t,room_nol,room_no,L1,j,ratel,rate,da_l,da ,dd_l,dd,Submit,Update,cr
    rootR=tkinter.Tk()
    rootR.title("ROOM ALLOCATION")
    rootR.geometry("500x400")
    rootR.configure(background='cyan4')
    
    r_head=tkinter.Label(rootR,text="ROOM ALLOCATION",bg='white',fg='cyan4',font="Times 16 bold italic",height=1)
    r_head.place(x=0,y=0)
    id=tkinter.Label(rootR,text="PATIENT ID",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    id.place(x=50,y=50)
    P_id=tkinter.Entry(rootR,fg='cyan4',width=20,font='Arial 12')
    P_id.place(x=250,y=50)
    room_tl=tkinter.Label(rootR,text="ROOM TYPE",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    room_tl.place(x=50, y=100)
    L=['SINGLE ROOM: Rs 4500','TWIN SHARING : Rs2500','TRIPLE SHARING: Rs2000']
    room_t= tkinter.Listbox(rootR,fg='cyan4',width=20,font='Arial 12', height=1, selectmode='SINGLE', exportselection=0)
    for i in L:
        room_t.insert(tkinter.END,i)
    room_t.place(x=250,y=100)
    room_nol=tkinter.Label(rootR,text="ROOM NUMBER",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    room_nol.place(x=50,y=150)
    L1=['101','102-AA','102-BB','103','104-AA','104-BB','105','206-AAA','206-BBB','206-CCC','207','208-AAA','208-BBB','208-CCC','210','211','302','304-AA','304-BB']
    room_no = tkinter.Listbox(rootR,fg='cyan4',width=20,font='Arial 12', height=1, selectmode='SINGLE', exportselection=0)
    for j in L1:
        room_no.insert(tkinter.END,j)
    room_no.place(x=250,y=150)
    ratel=tkinter.Label(rootR, text="ROOM CHARGES",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    ratel.place(x=50, y=200)
    rate=tkinter.Entry(rootR,fg='cyan4',width=20,font='Arial 12')
    rate.place(x=250, y=200)
    da_l = tkinter.Label(rootR, text="DATE ADMITTED",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    da_l.place(x=50,y=250)
    da=tkinter.Entry(rootR,fg='cyan4',width=20,font='Arial 12')
    da.place(x=250,y=250)
    dd_l = tkinter.Label(rootR, text="DATE DISCHARGED",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    dd_l.place(x=50, y=300)
    dd =tkinter.Entry(rootR,fg='cyan4',width=20,font='Arial 12')
    dd.place(x=250, y=300)
    Submit=tkinter.Button(rootR,text="SUBMIT",command=room_button,font="arial 12",bg='gray25',fg='white',height=1,width=10)
    Submit.place(x=50,y=350)
    Update=tkinter.Button(rootR,text="UPDATE",command=update_button,font="arial 12",bg='gray25',fg='white',height=1,width=10)
    Update.place(x=150,y=350)
    cr=tkinter.Button(rootR,text='SEARCH',command=R_search,font="arial 12",bg='gray25',fg='white',height=1,width=10)
    cr.place(x=250,y=350)
    ee=tkinter.Button(rootR,text="EXIT",command=exitt,font="arial 12",bg='gray25',fg='white',height=1,width=10)
    ee.place(x=350,y=350)
    rootR.mainloop()
