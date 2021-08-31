import tkinter
import tkinter.messagebox
from Patient_Registration import PAT
from Room_Registration import Room_all
from Billing_Form import BILLING
from Employee_Registration import emp_screen
from Appointment_Booking import appo

import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sood@123',
    database='HOSPITAL'
	)

if mydb:
    print('Connection successful !!!')
else:
    print('Connection failed !!!')

mycursor = mydb.cursor()

#variables
root1=None
rootp=None
pat_ID=None
pat_name=None
pat_dob=None
pat_address=None
pat_sex=None
pat_BG=None
pat_email=None
pat_contact=None
pat_contactalt=None
pat_CT=None


#EXIT for MENU
def ex():
    global root1
    root1.destroy()

#MENU BUTTONS
def menu():
    global root1,button1,button2,button3,button4,button5,m,button6
    root1=tkinter.Tk()
    root1.geometry("450x350")
    root1.configure(background='cyan4')
    root1.title("MAIN MENU")
    m=tkinter.Label(root1,text="ADMIN OPTIONS",bg='white',fg='cyan4',font="Times 16 bold italic",height=1)
    button1 = tkinter.Button(root1, text="1. PATIENT REGISTRATION",font="arial 12",bg='gray25',fg='white',height=1,width=40,command=PAT)
    button2 = tkinter.Button(root1, text="2. ROOM ALLOCATION",font="arial 12",bg='gray25',fg='white',height=1,width=40,command=Room_all)
    button3 = tkinter.Button(root1, text="3. EMPLOYEE REGISTRATION",font="arial 12",bg='gray25',fg='white',height=1,width=40,command=emp_screen)
    button4 = tkinter.Button(root1, text="4. BOOK APPOINTMENT",font="arial 12",bg='gray25',fg='white',height=1,width=40,command=appo)
    button5 = tkinter.Button(root1, text="5. PATIENT BILL",font="arial 12",bg='gray25',fg='white',height=1,width=40,command=BILLING)
    button6 = tkinter.Button(root1, text="6. EXIT",font="arial 12",bg='gray25',fg='white',height=1,width=40,command=ex)
    m.place(x=0,y=0)
    button1.place(x=50,y=50)
    button2.place(x=50,y=100)
    button3.place(x=50,y=150)
    button4.place(x=50, y=200)
    button5.place(x=50,y=250)
    button6.place(x=50,y=300)
    root1.mainloop()


