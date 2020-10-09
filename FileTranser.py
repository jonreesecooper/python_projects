import shutil
import os
import time
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master=master
        self.master.minsize(440,320)
        self.master.maxsize(440,320)
        self.master.title("Daily File Transfer")
        self.master.configure(bg="#F0F0F0")
        self.label_1=tk.Label(self.master,text="Select source filepath")
        self.label_1.grid(row=0,column=0,padx=(15,0),pady=(10,0), sticky=W)
        self.btn1 = tk.Button(self.master,width=12,height=1,text="Source",command=lambda: getDir(self))
        self.btn1.grid(row=1,column=0,padx=(15,0),pady=(10,0), sticky=W)
        self.text1 = tk.Text(self.master,width=50,height=2,)
        self.text1.grid(row=2,column=0,padx=(15,15),pady=(10,0))
        self.label_2=tk.Label(self.master,text="Select destination filepath")
        self.label_2.grid(row=3,columnspan=2,padx=(15,0),pady=(10,0),sticky=W)
        self.btn2 = tk.Button(self.master,width=12,height=1,text="Destination",command=lambda: setDir(self))
        self.btn2.grid(row=4,column=0,padx=(15,0),pady=(10,0), sticky=W)
        self.text2 = tk.Text(self.master,width=50,height=2,)
        self.text2.grid(row=5,column=0,padx=(15,15),pady=(10,0))
        self.label_3=tk.Label(self.master,text="Run File Transfer")
        self.label_3.grid(row=6,column=0,padx=(15,0),pady=(10,0),sticky=W)
        self.btn3 = tk.Button(self.master,width=12,height=2,text="Run",command=lambda: timestamp(self))
        self.btn3.grid(row=7,column=0,padx=(15,0),pady=(10,0), sticky=W)


def getDir(self):
    source = tk.filedialog.askdirectory()
    for data in source:
        self.text1.insert(END,data[0])

def setDir(self):
    destination = tk.filedialog.askdirectory()
    for data in destination:
       self.text2.insert(END,data[0])

def listoffiles(self):
    check = os.listdir(path = self.text1.get())
    return check

def timestamp(self):
    check = listoffiles(self)
    newlist = []
    i = 0
    while i < len(check):
        abPath=os.path.join(source,check[i])
        result = abPath.endswith('txt')
        
        if result:
            mod_time = os.path.getmtime(abPath)
            cur_time = time.time()
            if mod_time >= (cur_time - 86400):
                newlist.append(check[i])
        i += 1
    for i in newlist:
        shutil.move(source+i,self.text2.get())
    try:
        notify = messagebox.showinfo("File Transfer Complete", "You may now close application")
        return notify
    except:
        pass



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()