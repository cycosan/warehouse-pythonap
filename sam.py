from tkinter import*
from tkinter import ttk
from tkinter.ttk import Treeview
class product:

        def __init__(self, root):
            self.root = root
            self.root.title("WAREHOUSE MANAGEMENT SYSTEM")
            self.root.geometry("1300x700+0+0")
            self.root.resizable(False, False)
            self.root.config(bg="lavender")

           #main frame
            MainFrame=Frame(self.root,bg="black")
            MainFrame.grid()
            self.title=Label(MainFrame,font=("bahnschrift",50,"bold"),fg="black",
                              text="                             JUSAN WAREHOUSE  ",bg="lavender")
            self.title.grid()
            #data frame
            DataEntryFrame = Frame(self.root, bg="lavender", relief=GROOVE, borderwidth=1)
            DataEntryFrame.place(x=10, y=5, width=450, height=700, )
            self.Title = Label(DataEntryFrame, font=("Goudy old style", 25, "bold"), fg="black",
                               text="        Enter items",
                               bg=("lavender"))
            self.Title.grid()

            #label for item name
            self.item_name = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="ITEM NAME:"
                                        , fg="black", bg="lavender").place(x=10, y=80)
            self.txt_itemname = Entry(DataEntryFrame, font=("Goudy old style", 12), bg="white")
            self.txt_itemname.place(x=200, y=80, width=200, height=25)

            #label for manufacture
            self.lblmanufacture = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="MANUFACTURE:"
                                      , fg="black", bg="lavender").place(x=10, y=120)
            self.txt_manufacture = Entry(DataEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_manufacture.place(x=200, y=120, width=200, height=25)

            #label for item category
            self.lblitemcategory = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="ITEM CATEGORY:"
                                         , fg="black", bg="lavender").place(x=10, y=160)
            self.cboitemcategory=ttk.Combobox(DataEntryFrame,font=('bahnscrift',15,"bold"),state='readonly,width=50')
            self.cboitemcategory['value']=('',"food","Vechicle","makeup","clothes","things")
            self.cboitemcategory.place(x=200,y=160,width=200,height=25)

            #label for quantity
            self.lblquantity = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="QUANTITY:"
                                        , fg="black", bg="lavender").place(x=10, y=200)
            self.txt_quantity = Entry(DataEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_quantity.place(x=200, y=200, width=200, height=25)

            #label for price
            self.lblprice = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="PRICE(rps):"
                                     , fg="black", bg="lavender").place(x=10, y=240)
            self.txt_price = Entry(DataEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_price.place(x=200, y=240, width=200, height=25)

            # label for color
            self.lblcolor = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="COLOR:"
                                  , fg="black", bg="lavender").place(x=10, y=280)
            self.txt_color = Entry(DataEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_color.place(x=200, y=280, width=200, height=25)

             # labek for weight
            self.lblweight = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="WEIGHT(kgs):"
                                  , fg="black", bg="lavender").place(x=10, y=320)
            self.txt_weight = Entry(DataEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_weight.place(x=200, y=320, width=200, height=25)

            #label for date
            self.lblEnterDate= Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="ENTER DATE:"
                                  , fg="black", bg="lavender").place(x=10, y=360)
            self.txt_EnterDate= Entry(DataEntryFrame, font=("Goudy old style", 15), bg="white")
            self.txt_EnterDate.place(x=200, y=360, width=200, height=25)

             #label for recieve
            self.lblreceive = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="RECIEVE:"
                                         , fg="black", bg="lavender").place(x=10, y=400)
            self.cboreceive = ttk.Combobox(DataEntryFrame, font=('bahnscrift', 15, "bold"),
                                                state='readonly,width=50')
            self.cboreceive['value'] = ('', "recieve","not recieve")
            self.cboreceive.place(x=200, y=400, width=200, height=25)

            #button for add, delete , update , clear
            self.b1 = Button(text="ADD", font=('bahnschrift', 15, 'bold'))
            self.b1.place(x=50, y=500)
            self.b2 = Button(text="DELETE", font=('bahnschrift', 15, 'bold'))
            self.b2.place(x=50, y=600)

            self.b3= Button(text="UPDATE", font=('bahnschrift', 15, 'bold'))
            self.b3.place(x=250, y=500)
            self.b3 = Button(text="CLEAR", font=('bahnschrift', 15, 'bold'))
            self.b3.place(x=250, y=600)

           #data drame
            ShowdataFrame = Frame(self.root, bg="lavender", relief=GROOVE, borderwidth=1)
            ShowdataFrame.place(x=500, y=80, width=780, height=600)
            scroll_x = Scrollbar(ShowdataFrame, orient=HORIZONTAL)
            scroll_y = Scrollbar(ShowdataFrame, orient=VERTICAL)
            Student_table =ttk.Treeview(ShowdataFrame, column=("item name", "manufacture", "item category", "quantity", "price","color", "weight", "enter date", "status")
                                       , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=Student_table.xview)
            scroll_y.config(command=Student_table.yview)
            Student_table.heading("item name",text="item name")
            Student_table.heading("manufacture", text="manufacture")
            Student_table.heading("item category", text="item category")
            Student_table.heading("quantity", text="quantity")
            Student_table.heading("price", text="price")
            Student_table.heading("color",text="color")
            Student_table.heading("weight", text="weight")
            Student_table.heading("enter date", text="enter date")
            Student_table.heading("status", text="status")
            Student_table['show']="headings"
            Student_table.pack(fill=BOTH,expand=1)
            Student_table.pack()
if __name__ =='__main__':
    root=Tk()
    application=product (root)
    root.mainloop()