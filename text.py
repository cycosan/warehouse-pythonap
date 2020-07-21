from tkinter import*
from tkinter import ttk
from tkinter.ttk import Treeview
class product:

        def __init__(self, root):
            self.root = root
            self.root.title("WAREHOUSE MANAGEMENT SYSTEM")
            self.root.geometry("1300x700+0+0")
            self.root.resizable(False, False)
            self.root.config(bg="light grey")
            #main frame and title
            MainFrame=Frame(self.root,bg="black")
            MainFrame.grid()
            self.title=Label(MainFrame,font=("bahnschrift",50,"bold"),fg="black",
                              text="                             JUSAN WAREHOUSE  ",bg="light grey")
            self.title.grid()

           #frame for customer details
            JusanEntryFrame = Frame(self.root, bg="light grey", relief=GROOVE, borderwidth=1)
            JusanEntryFrame.place(x=10, y=5, width=450, height=700, )
            self.Title = Label(JusanEntryFrame, font=("Goudy old style", 25, "bold"), fg="black",
                               text="        CUSTOMER DETAILS",
                               bg=("light grey"))
            self.Title.grid()

            #label for customer id
            self.item_name = Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="CUSTOMER ID:"
                                        , fg="black", bg="light grey").place(x=10, y=80)
            self.txt_itemname = Entry(JusanEntryFrame, font=("Goudy old style", 12), bg="white")
            self.txt_itemname.place(x=200, y=80, width=200, height=25)

            #label for customer name
            self.lblmanufacture = Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="CUSTOMER NAME:"
                                      , fg="black", bg="light grey").place(x=10, y=120)
            self.txt_manufacture = Entry(JusanEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_manufacture.place(x=200, y=120, width=200, height=25)

            #label for item name
            self.lblitemcategory = Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="ITEMS NAME:"
                                         , fg="black", bg="light grey").place(x=10, y=160)
            self.cboitemcategory=ttk.Combobox(JusanEntryFrame,font=('bahnscrift',15,"bold"),state='readonly,width=50')
            self.cboitemcategory['value']=('',"food","Vechicle","makeup","clothes","things")
            self.cboitemcategory.place(x=200,y=160,width=200,height=25)


            #label for location
            self.lblquantity = Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="LOCATION:"
                                        , fg="black", bg="light grey").place(x=10, y=200)
            self.txt_quantity = Entry(JusanEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_quantity.place(x=200, y=200, width=200, height=25)

            #label for price
            self.lblprice = Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="PRICE(rps):"
                                     , fg="black", bg="light grey").place(x=10, y=240)
            self.txt_price = Entry(JusanEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_price.place(x=200, y=240, width=200, height=25)

            #label for quantity
            self.lblcolor = Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="QUANTITY:"
                                  , fg="black", bg="light grey").place(x=10, y=280)
            self.txt_color = Entry(JusanEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_color.place(x=200, y=280, width=200, height=25)

            #label for distance
            self.lblweight = Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="DISTANCE:"
                                  , fg="black", bg="light grey").place(x=10, y=320)
            self.txt_weight = Entry(JusanEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_weight.place(x=200, y=320, width=200, height=25)

            #label for total
            self.lblEnterDate= Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="TOTAL:"
                                  , fg="black", bg="light grey").place(x=10, y=360)
            self.txt_EnterDate= Entry(JusanEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_EnterDate.place(x=200, y=360, width=200, height=25)

            #label for date
            self.lblEnterDate = Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="DATE:"
                                      , fg="black", bg="light grey").place(x=10, y=400)
            self.txt_EnterDate = Entry(JusanEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_EnterDate.place(x=200, y=400, width=200, height=25)

            #label for deliver
            self.lblreceive = Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="DELIEVER:"
                                         , fg="black", bg="light grey").place(x=10, y=440)
            self.cboreceive = ttk.Combobox(JusanEntryFrame, font=('bahnscrift', 15, "bold"),
                                                state='readonly,width=50')
            self.cboreceive['value'] = ('', "deliever","not deliever")
            self.cboreceive.place(x=200, y=440, width=200, height=25)

            #buttons
            self.b1 = Button(text="ADD", font=('bahnschrift', 15, 'bold'))
            self.b1.place(x=50, y=550)
            self.b2 = Button(text="DELETE", font=('bahnschrift', 15, 'bold'))
            self.b2.place(x=50, y=650)

            self.b3= Button(text="UPDATE", font=('bahnschrift', 15, 'bold'))
            self.b3.place(x=250, y=550)
            self.b3 = Button(text="CLEAR", font=('bahnschrift', 15, 'bold'))
            self.b3.place(x=250, y=650)

            #dataframe
            samdataFrame = Frame(self.root, bg="lavender", relief=GROOVE, borderwidth=1)
            samdataFrame.place(x=500, y=80, width=780, height=600)
            scroll_x = Scrollbar(samdataFrame, orient=HORIZONTAL)
            scroll_y = Scrollbar(samdataFrame, orient=VERTICAL)
            San_table =ttk.Treeview(samdataFrame, column=("customer id", "customer name", "item name","location","quantity", "price","distance", "total", " date", "status")
                                       , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=San_table.xview)
            scroll_y.config(command=San_table.yview)
            San_table.heading("customer id",text="customer id")
            San_table.heading("customer name", text="customer name")
            San_table.heading("item name", text="item name")
            San_table.heading("location", text="location")

            San_table.heading("quantity", text="quantity")
            San_table.heading("price", text="price")
            San_table.heading("distance",text="distance")
            San_table.heading("total", text="total")
            San_table.heading(" date", text=" date")
            San_table.heading("status", text="status")
            San_table['show']="headings"
            San_table.pack(fill=BOTH,expand=1)
            San_table.pack()
if __name__ =='__main__':
    root=Tk()
    application=product (root)
    root.mainloop()
