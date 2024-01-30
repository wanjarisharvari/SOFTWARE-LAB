from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.ttk import *

root = Tk()
root.geometry("644x344")


user = []
teacher = []
ug = []
pg = []



class user(Tk) :
    def __init__ (self, userid ):
        self.geometry("644x344")
        self.userid = userid
        self.password = check_password()
        self.authenticated = False
        self.attempts = 3 
        self.active = True

    def authentication(self , userpass):
        if (self.attempts > 0 and userpass == self.password):
            self.authenticated = True
            self.attempts = 3
            return True
        else :
            self.attempts = self.attempts-1
            self.authenticated = False
            if self.attempts == 0:
                self.active = False
            return False
        
    def deregister(self):
        self.active = False
    
    


def check_password():
    while True:
        password = input("ReEnter a password: ")

        if (
            8 <= len(password) <= 12 and
            any(char.islower() for char in password) and
            any(char.isupper() for char in password) and
            any(char.isdigit() for char in password) and
            any(char in "!@#$%&*" for char in password) and
            " " not in password
        ):
            return password
        else:
            print("Invalid password. Please follow the password criteria.") 
    
    
    
    

'''class person():
    def __init__(self,name,userid,password):
        self.name = name
        self.userid = userid
        self.password = password'''


class teacher:
    def __init__(self,master,name,userid,password):
            self.master = master
            self.name = name
            self.userid = userid
            self.password = password
            self.administrator = "teacher"
            self.master.title("User registration for teacher")

    def create(self):
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


 
   
    def register(self,name,userid,password):
        pass
    def update(self, name , userid , password):
        self.name = name
        self.password = password
        self.userid = userid



class student:
    def __init__(self,name,userid,password,rollnumber):
        self.name = name
        self.userid = userid
        self.password = password
        self.administrator = "student"
        self.rollnumber = rollnumber

class ug(student):
    def __init__(self,name,userid,password,rollnumber,year,cg):
        student.__init__(self,name,userid,password,rollnumber)
        self.year = year
        self.course = "UG"
        self.cg = cg

        def update(self, name , userid , password,rollnumber,year,cg):
            self.name = name
            self.userid = userid
            self.password = password
            self.rollnumber = rollnumber
            self.cg = cg
            

class pg(student):
    def __init__(self,name,userid,password,rollnumber,year,cg):
        student.__init__(self,name,userid,password,rollnumber)
        self.year = year
        self.course = "PG"  
        self.cg = cg  

    def update(self, name , userid , password,rollnumber,year,cg):
            self.name = name
            self.userid = userid
            self.password = password
            self.rollnumber = rollnumber
            self.cg = cg

def typesignup():
        if(typevar.get() == "teacher" ):
            print("hi")
            
        if(typevar.get() == "ug_student"):
            print("hi")

        if(typevar.get() == "pg_student"):
            print("hi")
            

def signup():
    #if(uservalue.get() in user.userid):
     #   tmsg.showinfo("Registration status","You are already registered.")
    #else :
        #signup = Toplevel(root)
        signup = Tk()
        signup.geometry("644x344")
        global typevar
        typevar = StringVar()
        typevar.set("Radio")
        Label(signup, text = "Select the type of user.").grid(row=0, column=3)
        radio = Radiobutton(signup, text="Teacher", variable=typevar, value="teacher").grid(row=1, column=3)
        radio = Radiobutton(signup, text="UG Student", variable=typevar, value="ug_student").grid(row=2, column=3)
        radio = Radiobutton(signup, text="PG Student", variable=typevar, value="pg_student").grid(row=3, column=3)
        Button(typesignup,text="Submit").grid(row=4, column=3)
        signup.mainloop()

        
def login():
    pass

#if __name__ == "__main__":

#root = Tk()
#root.geometry("644x344")

Label(root, text="Enter user details").grid(row=0, column=3)


userid = Label(root, text="UserID")
password = Label(root, text="Password")


userid.grid(row=1, column=2)
password.grid(row=2, column=2)

 
uservalue = StringVar()
passvalue = StringVar()


userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)


userentry.grid(row=1, column=3)
passentry.grid(row=2, column=3)

Button(text="Signup", command = signup).grid(row=7, column=3)
Button(text="Login",command = login).grid(row=7, column=4)

 


root.mainloop()
 
