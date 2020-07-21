from tkinter import*
from tkinter import ttk
from tkinter.ttk import Treeview
class product:

        def __init__(self, root):
            self.root = root
            self.root.title("WAREHOUSE MANAGEMENT SYSTEM")
            self.root.geometry("1000x700+0+0")
            self.root.resizable(False, False)
            self.root.config(bg="alice blue")
            MainFrame=Frame(self.root,bg="black")
            MainFrame.grid()
            self.title=Label(MainFrame,font=("Goudy old style",50,"bold"),fg="black",
                              text="      JUSAN WAREHOUSE  ",bg="alice blue")

            self.title.grid()
            #frame
            DataEntryFrame=Frame(self.root,bg="alice blue",relief=GROOVE,borderwidth=0)
            DataEntryFrame.place(x=10,y=80,width=500,height=600,)

            #label and data entry for company detail
            self.Title=Label( DataEntryFrame,font=("Goudy old style",25,"bold"),fg="black",text="        COMPANY DETAIL",
                              bg="alice blue")
            self.Title.grid()

            #label and data entry for company name
            self.lblcompanyname = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="COMPANY NAME:"
                                 , fg="black", bg="alice blue").place(x=10, y=80)
            self.txt_companyname = Entry(DataEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_companyname.place(x=200, y=80, width=250, height=35)

            #label and data entry for contact no
            self.lblcontactno= Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="CONTACT NO:"
                                        , fg="black", bg="alice blue").place(x=10, y=140)
            self.txt_contactno = Entry(DataEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_contactno.place(x=200, y=140, width=250, height=35)

            #label and data entry for email address
            self.lblemailaddress= Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="EMAIL ADDRESS:"
                                      , fg="black", bg="alice blue").place(x=10, y=190)
            self.txt_emailaddress = Entry(DataEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_emailaddress.place(x=200, y=190, width=250, height=35)

            #label and data entry for location
            self.lbllocation = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="LOCATION:"
                                         , fg="black", bg="alice blue").place(x=10, y=240)
            self.txt_location = Entry(DataEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_location.place(x=200, y=240, width=250, height=35)

            #button
            self.b1 = Button(text="UPDATE", font=('bahnschrift', 15, 'bold'),bg="white")
            self.b2 = Button(text="ADD", font=('bahnschrift', 15, 'bold'),bg="white")
            self.b3 = Button(text="DELETE", font=('bahnschrift', 15, 'bold'),bg="white")
            self.b4 = Button(text="CLEAR", font=('bahnschrift', 15, 'bold'),bg="white")
            self.b5 = Button(text="BACK", font=('bahnschrift', 15, 'bold'),bg="white")
            self.b1.place(x=50, y=430)
            self.b2.place(x=300,y=430)
            self.b3.place(x=50,y=500)
            self.b4.place(x=300,y=500)
            self.b5.place(x=50,y=580)

            ShowdataFrame= Frame(self.root, bg="alice blue", relief=GROOVE, borderwidth=5)
            ShowdataFrame.place(x=500, y=80, width=500, height=600)
            scroll_x = Scrollbar(ShowdataFrame, orient=HORIZONTAL)
            scroll_y = Scrollbar(ShowdataFrame, orient=VERTICAL)
            San_table = ttk.Treeview(ShowdataFrame, column=("Company name", "contact no", "email address", "location"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=San_table.xview)
            scroll_y.config(command=San_table.yview)
            San_table.heading("Company name", text="Company name")
            San_table.heading("contact no", text="contact no")
            San_table.heading("email address", text="email address")
            San_table.heading("location", text="location")

            San_table.heading("location", text="location")

            San_table['show'] = "headings"
            San_table.pack(fill=BOTH, expand=1)
            San_table.pack()



root=Tk()
product(root)
root.mainloop()