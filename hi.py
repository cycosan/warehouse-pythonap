from tkinter import*
from tkinter import ttk
from tkinter.ttk import Treeview
class product:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.resizable(False, False)
        self.root.config(bg="sky blue")
        cusdataFrame = Frame(self.root, bg="orange", relief=GROOVE, borderwidth=1)
        MainFrame = Frame(self.root, bg="black")
        MainFrame.grid()
        self.title = Label(MainFrame, font=("bahnschrift", 25, "bold"), fg="white",
                           text="            Item Delivered                                                            Item Received ", bg="sky blue")
        self.title.grid()

        cusdataFrame.place(x=660, y=70, width=600, height=620)
        scroll_x = Scrollbar(cusdataFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(cusdataFrame, orient=VERTICAL)
        San_table = ttk.Treeview(cusdataFrame, column=("item name","price","quantity","company name")
                                 , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=San_table.xview)
        scroll_y.config(command=San_table.yview)
        San_table.heading("item name", text="item name")
        San_table.heading("price", text="price")
        San_table.heading("quantity", text="quantity")
        San_table.heading("company name", text="company name")

        San_table['show'] = "headings"
        San_table.pack(fill=BOTH, expand=1)
        San_table.pack()

        cacdataFrame = Frame(self.root, bg="red", relief=GROOVE, borderwidth=1)
        cacdataFrame.place(x=45, y=70, width=600, height=620)
        scroll_x = Scrollbar(cacdataFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(cacdataFrame, orient=VERTICAL)
        Sak_table = ttk.Treeview(cacdataFrame, column=("item name", "price", "quantity", "customer name")
                                 , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=Sak_table.xview)
        scroll_y.config(command=Sak_table.yview)
        Sak_table.heading("item name", text="item name")
        Sak_table.heading("price", text="price")
        Sak_table.heading("quantity", text="quantity")
        Sak_table.heading("customer name", text="customer name")

        Sak_table['show'] = "headings"
        Sak_table.pack(fill=BOTH, expand=1)
        Sak_table.pack()


if __name__ =='__main__':
    root=Tk()
    application=product (root)
    root.mainloop()



