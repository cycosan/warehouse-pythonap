from tkinter import*
from PIL import ImageTk

from home import product
from tkinter import messagebox
import mysql.connector
try:
    mydb1=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='gg'
    )
    mycursor=mydb1.cursor()


except mysql.connector.Error as error:
    messagebox.showinfo("Information", "No Server Connection")
    exit(0)
class Please_Login:

    def __init__ (self,root):
        self.root=root
        self.root.title("Please Login")
        self.root.geometry("640x426+100+50")
        self.root.resizable(False, False)
        # self.bg=ImageTk.PhotoImage(file='Desktop/sanju.jpg')
        # self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        global usename1
        global rollno1
        #frame login
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=305,y=70, height=340, width=320)

        #label for interface heading
        title = Label(Frame_login, text="LOGIN SYSTEM !!", font=("bahnschrift", 15, "bold"),
                      fg="black", bg="white").place(x=10, y=20)
        sam = Label(Frame_login, text="please login in here", font=("arial", 12, "bold"),
                    fg="black", bg="white").place(x=10, y=50)
        self.namevar=StringVar()
        self.pwvar=StringVar()
        #label and entry for username
        self.lbluser = Label(Frame_login, font=('Bahnschrift', 12, "bold"), text="USER NAME:"
                             , fg="black", bg="white").place(x=10, y=90)
        self.txt_username = Entry(Frame_login, font=("Goudy old style", 15), bg="lavender",textvariable=self.namevar)
        self.txt_username.place(x=130, y=90, width=170, height=25)

        #label and entry for password
        self.lbluser = Label(Frame_login, font=('Bahnschrift', 12, "bold"), text="PASSWORD:"
                             , fg="black", bg="white").place(x=10, y=130)
        self.txt_userpw = Entry(Frame_login, font=("Goudy old style", 15), bg="LAVENDER",textvariable=self.pwvar,show="*")
        self.txt_userpw.place(x=130, y=130, width=170, height=25)

        #login button
        self.login = Button(self.root, text="LOGIN", bg="white", fg="black",command=self.loginAdd,
        font=("Bahnschrift", 15, "bold"))
        self.login.place(x=330, y=250, width=250,height=30)

        #sign up button
        signup=Button(self.root,text="SIGN UP",bg="white",fg="black",
                     font=("Bahnschrift",15,"bold")).place(x=330, y=290, width=250, height=30)

        #reset button
        reset= Button(self.root, text="RESET", bg="white", fg="black",
                        font=("Bahnschrift", 15, "bold")).place(x=330, y=330, width=250, height=30)

        # forget password button
        forget = Button(Frame_login, text="Forget Password?", bg="white", fg="black", bd=0,
                        font=("Bahnschrift", 10, "bold")).place(x=10, y=310)
    def loginAdd(self):
        username1 = self.txt_username.get()
        rollno1 = self.txt_userpw.get()
        sql="SELECT * FROM login where username=%s"
        value=(username1,)

        mycursor.execute(sql, value)
        myresult = mycursor.fetchall()
        for i in myresult:
            id = i[0]
            pw = i[1]

        if (username1 == "" or rollno1 == ""):
            messagebox.showinfo("Information", "Fill all the fields")

        elif (username1==id and rollno1==pw):
            self.reg = Toplevel(self.root)
            product(self.reg)
        else:
            messagebox.showinfo("Information","enter correct password and username")







root=Tk()
Please_Login(root)
root.mainloop()