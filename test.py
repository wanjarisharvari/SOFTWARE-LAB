'''class person():
    def __init__(self,name,userid,password):
        self.name = name
        self.userid = userid
        self.password = password'''
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.ttk import *

class teacher:
    def __init__(self,master,name,userid,password):
            self.master = master
            self.geometry("644x344")
            self.name = name
            self.userid = userid
            self.password = password
            self.administrator = "teacher"
            self.master.title("User registration for teacher")

    
    #def create(self):
            self.namevar = StringVar()
            self.useridvar = StringVar()
            self.passwordvar = StringVar()

            #self.text = Label(self.master, text="Enter user details").grid(row=0, column=3)

            self.name = Label(self.master, text = "Name")
            self.userid = Label(self.master , text = "UserID")
            self.password = Label(self.master , text ="Password")

            self.nameentry = Entry(self.master, textvariable=self.namevar)
            self.userentry = Entry(self.master , textvariable=self.useridvar)
            self.passentry = Entry(self.master, textvariable=self.passwordvar)

root = Tk()
app = teacher(root)
root.mainloop()
