from tkinter import *
import tkinter as tk

import phonebook_main
import phonebook_func

def load_gui(self):
    #   defining all of our labels, and setting them with grid
    self.lbl_fname = tk.Label(self.master,text="First Name: ")
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_lname = tk.Label(self.master,text="Last Name: ")
    self.lbl_lname.grid(row=2, column=0, padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_phone = tk.Label(self.master,text="Phone Number: ")
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_email = tk.Label(self.master, text="Email address: ")
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_user = tk.Label(self.master,text="User: ")
    self.lbl_user.grid(row=0, column=2, padx=(0,0),pady=(10,0),sticky=N+W)

    #   defining all of our entry fields and setting them on the grid
    self.txt_fname = tk.Entry(self.master, text="")
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master, text="")
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master, text="")
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_email = tk.Entry(self.master, text="")
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    #Define the listbox with a scrollbar and grid them
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    #   exportselection is used so that more than one widget can be highlighted at a time
    #   essentialy, setting it to zero makes it false, which allows other widgets to be highlighted
    #   while keeping the listbox highlighted as well.  Otherwise, if you selected another
    #   widget the highlighted aspects of listbox would no longer be hightlighted
    #   yscrollcommand=self.scrollbar links the scrolling of lstList1 to the actions of scrollbar1
    #   it affects the vertical scrolling and ties it to our scroll bar
    self.lstList1.bind('<<ListboxSelect>>',lambda event: drill50_phonebook_func.onSelect(self,event))
    #   Binding to our listbox an event, bind is a listener, if somebody clicks
    #   on anything in the list, it calls onSelect function
    #   the lambda ensures that the function only occurs when called on, not automatically
    #   AWAITING ANSWER ON LISTBOXSELECTION FROM SEAN
    self.scrollbar1.config(command=self.lstList1.yview)
    #   this is configuring the scrollbar to affect the vertical view of our lstList1
    self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),stick=N+E+S)
    self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    # creating each button, setting the text in it, and the function it will call when clicked
    self.btn_add = tk.Button(self.master,width=12,height=2,text="Add",command=lambda: phonebook_func.addToList(self))
    self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.btn_update = tk.Button(self.master,width=12,height=2,text="Update",command=lambda: phonebook_func.onUpdate(self))
    self.btn_update.grid(row=8,column=1,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_delete = tk.Button(self.master,width=12,height=2,text="Delete",command=lambda: phonebook_func.onDelete(self))
    self.btn_delete.grid(row=8,column=2,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text="Close",command=lambda: phonebook_func.ask_quit(self))
    self.btn_close.grid(row=8,column=4,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)

    phonebook_func.create_db(self)
    phonebook_func.onRefresh(self)


if __name__ == "__main__":
    pass
    
