from tkinter import*
from PIL import ImageTk
import company
import manifest
class product:

        def __init__(self, root):
            self.root = root
            self.root.title("WAREHOUSE MANAGEMENT SYSTEM")
            self.root.geometry("1024x768+0+0")
            self.root.resizable(False, False)
            # self.bg = ImageTk.PhotoImage(file='Desktop/hello.jpg')
            # self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
            self.b1=Button (self.root,text="COMPANY",command=self.addcompany,font=('bahnschrift',20,'bold'))
            self.b2 = Button(self.root,text="MAINFEST",command=self.addcompany,font=('bahnschrift',20,'bold'))
            self.b3 = Button(self.root,text="WAREHOUSE",font=('bahnschrift',20,'bold'))
            self.b4 = Button(self.root,text="UPDATE",font=('bahnschrift',20,'bold'))
            self.b5 = Button(self.root,text="SHIPMENT",font=('bahnschrift',20,'bold'))
            self.b6 = Button(self.root,text="QUIT",font=('bahnschrift',20,'bold'))
            self.b1.place(x=30, y=50)
            self.b2.place(x=30,y=150)
            self.b3.place(x=30, y=250)
            self.b4.place(x=30, y=350)
            self.b5.place(x=30, y=450)
            self.b6.place(x=30, y=550)

        def addcompany(self):
            self.reg = Toplevel(self.root)
            company.product(self.reg)

        def addmanifest(self):
            self.reg = Toplevel(self.root)
            manifest.product(self.reg)


if __name__ =='__main__':
    root=Tk()
    product(root)
    root.mainloop()