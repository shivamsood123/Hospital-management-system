import tkinter
from Menu_Window import menu

#root=login page
#root1=menu
#rootp=patient form

#variables
root=None
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None

#command for login button
def GET():
    global userbox,passbox,error,root
    S1=userbox.get()
    S2=passbox.get()
    if(S1=='swapnil' and S2=='12345'):
        menu()
    elif(S1=='shivam' and S2=='12345'):
        menu()
    elif(S1=='sachin' and S2=='12345'):
        menu()
    else:
        tkinter.messagebox.showinfo("HOSPITAL MANAGEMENT SYSTEM","Wrong Input !!!")
        

#LOGIN PAGE WINDOW
def Entry():
    global userbox,passbox,login,topframe,bottomframe,image_1
    root = tkinter.Tk()
    #root.geometry("280x250")
    frame = tkinter.Frame(root,width=500,height=225,bg='cyan4')
    frame.pack()
    heading = tkinter.Label(frame, text="WELCOME TO HOSPITAL MANAGEMENT SYSTEM",bg='white',fg='cyan4',font='Times 16 bold italic')
    username=tkinter.Label(frame,text="Enter Username :",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    userbox = tkinter.Entry(frame,bg='white',fg='cyan4',width=20,font='Arial 12')
    password=tkinter.Label(frame,text="Enter Password :",bg='gray25',fg='white',height=1,width=20,font='Arial 12')
    passbox = tkinter.Entry(frame,show="*",fg='cyan4',width=20,font='Arial 12')
    login = tkinter.Button(frame, text="LOGIN", command=GET,font="arial 12",bg='gray25',fg='cyan4',height=1,width=40)
    heading.place(x=0,y=0)
    username.place(x=50,y=50)
    userbox.place(x=250,y=50)
    password.place(x=50,y=100)
    passbox.place(x=250,y=100)
    login.place(x=50,y=150)
    root.title("DATABASE LOGIN")
    root.mainloop()

Entry()

