#   Python Ver:     3.8.5
#   
#   Author:         Jonathan Cooper
#
#   Purpose:        Phonebook Demo.  Demonstrating OOP, Tkinter, GUI module
#                   using Tkinter Parent and Child relationships
#
#   Tested OS:      This code was written and tested to work with Windows 10

from tkinter import *
#   imports all modules from tkinter
import tkinter as tk
#   imports tkinter but gives it simpler name of tk

#   Be sure to import our other modules
#   So we can have access to them

import phonebook_gui
import phonebook_func

# Frame is the Tkinter frame class that our own class will inherit from
#ParentWindow is the child class we will use for our interface window
class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        #   gives set variables you can input when creating instance of ParentWindow
        #   args are arguments that can later be inputed
        #   kwargs are key value pair arguments that can later be inputed
        Frame.__init__(self, master, *args, **kwargs)

        #   define our master frame configuration
        self.master = master
        self.master.minsize(500,300)    #Height, width minimum size
        self.master.maxsize(500,300)    #Maximum size  
        #   This CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        #   accessing phonebook_func file and center_window function
        self.master.title("The Tkinter Phonebook Demo")
        #   Title of the window
        self.master.configure(bg="#F0F0F0")
        # sets a background color for our window

        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        #   lambdas are anyonymous functions, this one calls phonebook_function file
        #   and ask_quit function
        #   This protocol method is a tkinter built in method to catch if
        #   the user clicks the upper corner, X on windows OS.
        #   protocol makes a rule for the class to follow
        #   WM_DELETE_WINDOWS is the microsoft syntax for the closing X button

        phonebook_gui.load_gui(self)
        #   load in the GUI widgets from a separate module,
        #   keeping your code compartmentalized and clutter free

if __name__ == "__main__":
    root = tk.Tk() # syntax for creating window with tkinter
    App = ParentWindow(root) # naming our class as App, passes tkinter to it
    root.mainloop() # prevents window from automatically closing down, waits for instruction to do so
