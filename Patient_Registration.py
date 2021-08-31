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
rootU=None
rootD=None
rootS=None
head=None
inp_s=None
searchB=None
#display/search button

inp_d=None
entry1=None
errorD=None
disd1=None

#DELTE BUTTON
def Delete_button():
    global inp_d,entry1,errorD,disd1,mycursor,mydb
    inp_d = entry1.get()
    mycursor.execute("select * from PATIENT where PATIENT_ID=%s", (inp_d,))
    p=mycursor.fetchone()
    
    if (p==None):
        tkinter.messagebox.showinfo("HOSPITAL MANAGEMENT SYSTEM","PATIENT RECORD NOT FOUND")
        
    else:
        mycursor.execute("DELETE FROM CONTACT_NO where PATIENT_ID=%s",(inp_d,))
        mycursor.execute("DELETE FROM PATIENT where PATIENT_ID=%s",(inp_d,))
        tkinter.messagebox.showinfo("HOSPITAL MANAGEMENT SYSTEM","PATIENT RECORD DELETED")
        mydb.commit()


## DELETE SCREEN
def D_display():
    global rootD,headD,inp_d,entry1,DeleteB
    rootD=tkinter.Tk()
    rootD.geometry("250x200")
    rootD.title("DELETE WINDOW")
    rootD.configure(background='cyan4')
    headD=tkinter.Label(rootD,text="Enter Patient ID :",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    entry1=tkinter.Entry(rootD,bg='white',fg='cyan4',width=20,font='Arial 12')
    DeleteB=tkinter.Button(rootD,text="DELETE",command=Delete_button,font="arial 12",bg='gray25',fg='white',height=1,width=20)
    headD.place(x=25,y=25)
    entry1.place(x=25,y=75)
    DeleteB.place(x=25,y=125)
    rootD.mainloop()

p=None
#input patient form
def IN_PAT():
    global pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10,mycursor,mydb
    pp1=pat_ID.get()
    pp2=pat_name.get()
    pp3=pat_sex.get()
    pp4=pat_BG.get()
    pp5=pat_dob.get()
    pp6=pat_contact.get()
    pp7=pat_contactalt.get()
    pp8=pat_address.get()
    pp9=pat_CT.get()
    pp10=pat_email.get()
    n = (pp1,pp2,pp3,pp4,pp5,pp8,pp9,pp10,)
    mycursor.execute("INSERT INTO PATIENT(PATIENT_ID,NAME,SEX,BLOOD_GROUP,DOB,ADDRESS,CONSULT_TEAM,EMAIL) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",n)
    n1 = (pp1,pp6,pp7,)
    mycursor.execute("INSERT INTO CONTACT_NO VALUES (%s,%s,%s)",n1)
    tkinter.messagebox.showinfo("HOSPITAL DATABSE SYSTEM","DETAILS INSERTED INTO DATABASE")
    mydb.commit()


#exit from patient form
def EXO():
    rootp.destroy()

#function for patient form help
def nothing():
    tkinter.messagebox.showinfo("HOSPITAL DATABSE SYSTEM","CONTACT DATABASE HEAD :921 ")

def nothing1():
    tkinter.messagebox.showinfo("HOSPITAL DATABSE SYSTEM","MADE BY SWAPNIL VAISH, SHIVAM SOOD, SACHIN")

def P_search():
    global mycursor
    
    inp_s=pat_ID.get()
    mycursor.execute("select * from PATIENT where PATIENT_ID=%s",(inp_s,))
    p=mycursor.fetchone()
    
    if (p==None):
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM","PATIENT RECORD NOT FOUND")
    else:
        mycursor.execute("SELECT * FROM PATIENT NATURAL JOIN CONTACT_NO where PATIENT_ID=%s",(inp_s,))
        i=mycursor.fetchone()

        pat_name.delete(0,tkinter.END)
        pat_sex.delete(0,tkinter.END)
        pat_BG.delete(0,tkinter.END)
        pat_dob.delete(0,tkinter.END)
        pat_contact.delete(0,tkinter.END)
        pat_contactalt.delete(0,tkinter.END)
        pat_address.delete(0,tkinter.END)
        pat_CT.delete(0,tkinter.END)
        pat_email.delete(0,tkinter.END)
        
        pat_name.insert(0,i[1])
        pat_sex.insert(0,i[2])
        pat_BG.insert(0,i[3])
        pat_dob.insert(0,i[4])
        pat_contact.insert(0,i[8])
        pat_contactalt.insert(0,i[9])
        pat_address.insert(0,i[5])
        pat_CT.insert(0,i[6])
        pat_email.insert(0,i[7])
        
def P_update():
    global u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, ue1, mycursor, mydb
    u1 = pat_ID.get()
    u2 = pat_name.get()
    u3 = pat_sex.get()
    u4 = pat_dob.get()
    u5 = pat_BG.get()
    u6 = pat_contact.get()
    u7 = pat_contactalt.get()
    u8 = pat_email.get()
    u9 = pat_CT.get()
    u10 = pat_address.get()
    mycursor.execute("Select * from PATIENT where PATIENT_ID=%s", (u1,))
    p=mycursor.fetchone()
    
    if (p!=None):
        mycursor.execute("UPDATE PATIENT SET NAME=%s,SEX=%s,DOB=%s,BLOOD_GROUP=%s,ADDRESS=%s,CONSULT_TEAM=%s,EMAIL=%s where PATIENT_ID=%s", ( u2, u3, u4, u5, u10, u9, u8,u1,))
        mycursor.execute("UPDATE CONTACT_NO set CONTACTNO=%s,ALT_CONTACT=%s WHERE PATIENT_ID=%s", ( u6, u7,u1,))
        tkinter.messagebox.showinfo("HOSPITAL DATABSE SYSTEM", "DETAILS UPDATED INTO DATABASE")
        mydb.commit()

    else:
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "PATIENT IS NOT REGISTERED")


#PATIENT FORM
back=None
SEARCH=None
DELETE=None
UPDATE=None

def PAT():
    global pat_address, pat_BG, pat_contact, pat_contactalt, pat_CT, pat_dob, pat_email, pat_ID, pat_name, pat_sex
    global rootp,regform,id,name,dob,sex,email,ct,addr,c1,c2,bg,SUBMIT,menubar,filemenu,back,SEARCH,DELETE,UPDATE
    rootp=tkinter.Tk()
    rootp.title(" PATIENT REGISTRATION FORM")
    rootp.geometry("500x900")
    rootp.configure(background='cyan4')
    
    menubar=tkinter.Menu(rootp)
    
    filemenu=tkinter.Menu(menubar,tearoff=0)
    filemenu.add_command(label="NEW",command=PAT)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=EXO)
    
    helpmenu=tkinter.Menu(menubar,tearoff=0)
    helpmenu.add_command(label="HELP",command=nothing)
    helpmenu.add_command(label="ABOUT",command=nothing1)
    
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    rootp.config(menu=menubar)
    
    regform=tkinter.Label(rootp,text="REGISTRATION FORM",bg='white',fg='cyan4',font="Times 16 bold italic",height=1)
    id=tkinter.Label(rootp,text="PATIENT ID",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    pat_ID=tkinter.Entry(rootp,bg='white',fg='cyan4',width=20,font='Arial 12')
    name=tkinter.Label(rootp,text="PATIENT NAME",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    pat_name = tkinter.Entry(rootp,bg='white',fg='cyan4',width=20,font='Arial 12')
    sex=tkinter.Label(rootp,text="SEX",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    pat_sex=tkinter.Entry(rootp,bg='white',fg='cyan4',width=20,font='Arial 12')
    dob=tkinter.Label(rootp, text="DOB (YYYY-MM-DD)",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    pat_dob=tkinter.Entry(rootp,bg='white',fg='cyan4',width=20,font='Arial 12')
    bg=tkinter.Label(rootp, text="BLOOD GROUP",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    pat_BG=tkinter.Entry(rootp,bg='white',fg='cyan4',width=20,font='Arial 12')
    c1=tkinter.Label(rootp, text="CONTACT NUMBER",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    pat_contact=tkinter.Entry(rootp,bg='white',fg='cyan4',width=20,font='Arial 12')
    c2=tkinter.Label(rootp, text="ALTERNATE CONTACT",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    pat_contactalt=tkinter.Entry(rootp,bg='white',fg='cyan4',width=20,font='Arial 12')
    email=tkinter.Label(rootp, text="EMAIL",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    pat_email = tkinter.Entry(rootp,bg='white',fg='cyan4',width=20,font='Arial 12')
    ct=tkinter.Label(rootp,text="CONSULTING DOCTOR",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    pat_CT=tkinter.Entry(rootp,bg='white',fg='cyan4',width=20,font='Arial 12')
    addr=tkinter.Label(rootp, text="ADDRESS",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    pat_address=tkinter.Entry(rootp,bg='white',fg='cyan4',width=20,font='Arial 12')
    
    back=tkinter.Button(rootp,text="EXIT",command=EXO,font="arial 12",bg='gray25',fg='cyan4',height=1,width=40)
    SEARCH=tkinter.Button(rootp,text="  SEARCH  ",command=P_search,font="arial 12",bg='gray25',fg='white',height=1,width=10)
    DELETE=tkinter.Button(rootp,text="  DELETE  ",command=D_display,font="arial 12",bg='gray25',fg='white',height=1,width=10)
    UPDATE=tkinter.Button(rootp,text="  UPDATE  ",command=P_update,font="arial 12",bg='gray25',fg='white',height=1,width=10)
    SUBMIT=tkinter.Button(rootp,text="  SUBMIT  ",command=IN_PAT,font="arial 12",bg='gray25',fg='white',height=1,width=10)
    
    regform.place(x=0,y=0)
    id.place(x=50,y=50)
    pat_ID.place(x=250,y=50)
    name.place(x=50,y=100)
    pat_name.place(x=250,y=100)
    sex.place(x=50,y=150)
    pat_sex.place(x=250,y=150)
    dob.place(x=50,y=200)
    pat_dob.place(x=250,y=200)
    bg.place(x=50,y=250)
    pat_BG.place(x=250,y=250)
    c1.place(x=50,y=300)
    pat_contact.place(x=250,y=300)
    c2.place(x=50,y=350)
    pat_contactalt.place(x=250,y=350)
    email.place(x=50,y=400)
    pat_email.place(x=250,y=400)
    ct.place(x=50,y=450)
    pat_CT.place(x=250,y=450)
    addr.place(x=50,y=500)
    pat_address.place(x=250,y=500)
    
    SUBMIT.place(x=50,y=550)
    back.place(x=50,y=600)
    UPDATE.place(x=150,y=550)
    DELETE.place(x=250,y=550)
    SEARCH.place(x=350,y=550)
    
    rootp.mainloop()


