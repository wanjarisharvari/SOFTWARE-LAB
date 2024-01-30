from tkinter import *
import tkinter as tk
import tkinter.messagebox as tmsg
from tkinter.ttk import *

root = Tk()
root.geometry("644x344")
root.title("User Registration")

user_lst = []
teacher_lst = []
ug_lst = []
pg_lst = []



class user_object() :
    def __init__ (self, userid, password , admin ):
        self.userid = userid
        self.password = password
        self.admin = admin
        user_lst.append([userid,password,admin])
        #self.password = check_password()
        #self.authenticated = False
        #self.attempts = 3 
        #self.active = True

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
    
         
    

class person():
    def __init__(self,name,userid,password):
        self.name = name
        self.userid = userid
        self.password = password


class teacher_object():
    def __init__(self,name,userid,password):
        #person.__init__(self,name,userid,password)
        #super().__init__()
        self.name = name
        self.userid = userid
        self.password = password
        teacher_lst.append([name,userid,password])
        #self.admin = "teacher"
            
    
    def update(self, name , userid , password):
        self.name = name
        self.password = password
        self.userid = userid



class ug_object():
    def __init__(self,name,userid,password,rollnumber,year,cg):
        #student.__init__(self,name,userid,password,rollnumber)
        self.name = name
        self.userid = userid
        self.password = password
        self.rollnumber = rollnumber
        self.year = year
        self.cg = cg
        self.course = "UG"
        ug_lst.append([name,userid,password,rollnumber,year,cg,"UG"])

    def update(self, name , userid , password,rollnumber,year,cg):
            self.name = name
            self.userid = userid
            self.password = password
            self.rollnumber = rollnumber
            self.year = year
            self.cg = cg
            

class pg_object():
    def __init__(self,name,userid,password,rollnumber,year,cg):
        #student.__init__(self,name,userid,password,rollnumber)
        self.name = name
        self.userid = userid
        self.password = password
        self.rollnumber = rollnumber
        self.year = year
        self.course = "PG"  
        self.cg = cg 
        pg_lst.append([name,userid,password,rollnumber,year,cg,"PG"]) 

    def update(self, name , userid , password,rollnumber,year,cg,):
            self.name = name
            self.userid = userid
            self.password = password
            self.rollnumber = rollnumber
            self.year = year
            self.cg = cg
            

def signup_():

        signup = Toplevel(root)
        signup.title("Signup")
        def order():

            
                def check_password():
                    if (
                            8 <= len(passvalue.get()) <= 12 and
                            any(char.islower() for char in passvalue.get()) and
                            any(char.isupper() for char in passvalue.get()) and
                            any(char.isdigit() for char in passvalue.get()) and
                            any(char in "!@#$%&*" for char in passvalue.get()) and
                            (uservalue.get().endswith("@gmail.com"))
                            ):
                                tmsg.showinfo("result","Saved Successfully!")
                    else:
                            tmsg.showinfo("Result","Invalid password or User ID. Please follow the password criteria.")
                        
                if(typevar.get()==1):
                        teacher = Toplevel(signup)
                        teacher.title("Teacher")
                        teacher.geometry("644x344")
                        Label(teacher, text="Enter user details").grid(row=0, column=3)


                        name = Label(teacher, text="Name").grid(row=1, column=2)
                        userid = Label(teacher, text="UserID (email)").grid(row=2, column=2)
                        password = Label(teacher, text="Password").grid(row=3, column=2)

                        

                        namevalue = StringVar()
                        uservalue = StringVar()
                        passvalue = StringVar()


                        nameentry = Entry(teacher, textvariable=namevalue).grid(row=1, column=3)
                        userentry = Entry(teacher, textvariable=uservalue).grid(row=2, column=3)
                        passentry = Entry(teacher, textvariable=passvalue).grid(row=3, column=3)
                     
                        def submit_form():
                            # Retrieve values from StringVar variables when the form is submitted
                            name = namevalue.get()
                            userid = uservalue.get()
                            password = passvalue.get()
                            new_teacher = teacher_object(name,userid,password)

                        #teacher_lst.append([namevalue.get(),uservalue.get(),passvalue.get()])
                            new_user = user_object(uservalue.get(),passvalue.get(),"teacher")
                            print(teacher_lst)
                        #user_lst.append(new_user)
                        

                        Button(teacher,text="Submit",command=lambda: [check_password(), submit_form()]).grid(row=10, column=3)
                        #Button(text="Login",command = login).grid(row=7, column=4)
                        #tmsg.showinfo("result","hi")

                        teacher.mainloop()



                if(typevar.get()==2):
                        ugstudent = Toplevel(signup)
                        ugstudent.title("Ug Student")
                        ugstudent.geometry("644x344")
                        Label(ugstudent, text="Enter user details").grid(row=0, column=3)


                        name = Label(ugstudent, text="Name").grid(row=1, column=2)
                        userid = Label(ugstudent, text="UserID (email)").grid(row=2, column=2)
                        password = Label(ugstudent, text="Password").grid(row=3, column=2)
                        rollnumber = Label(ugstudent, text="RollNumber").grid(row=4, column=2)
                        year = Label(ugstudent, text="Year").grid(row=5, column=2)
                        cg = Label(ugstudent, text="CGPA").grid(row=6, column=2)


                        namevalue = StringVar()
                        uservalue = StringVar()
                        passvalue = StringVar()
                        rollvalue = StringVar()
                        yearvalue = StringVar()
                        cgvalue = StringVar()


                        nameentry = Entry(ugstudent, textvariable=namevalue).grid(row=1, column=3)
                        userentry = Entry(ugstudent, textvariable=uservalue).grid(row=2, column=3)
                        passentry = Entry(ugstudent, textvariable=passvalue).grid(row=3, column=3)
                        rollentry = Entry(ugstudent, textvariable=rollvalue).grid(row=4, column=3)
                        yearentry = Entry(ugstudent, textvariable=yearvalue).grid(row=5, column=3)
                        cgentry = Entry(ugstudent, textvariable=cgvalue).grid(row=6, column=3)


                        new_ug = ug_object(namevalue.get(),uservalue.get(),passvalue.get(),rollvalue.get(),yearvalue.get(),cgvalue.get())
                        #ug_lst.append(new_ug)
                        new_user = user_object(uservalue.get(),passvalue.get(),"ug_student")
                        #user_lst.append(new_user)



                        Button(ugstudent,text="Submit",command = check_password).grid(row=10, column=3)
                        #Button(text="Login",command = login).grid(row=7, column=4)
                        #tmsg.showinfo("result","hi")

                        ugstudent.mainloop()

                if(typevar == 3):
                        pgstudent = Toplevel(signup)
                        pgstudent.title("Pg Student")
                        pgstudent.geometry("644x344")
                        Label(pgstudent, text="Enter user details").grid(row=0, column=3)


                        name = Label(pgstudent, text="Name").grid(row=1, column=2)
                        userid = Label(pgstudent, text="UserID (email)").grid(row=2, column=2)
                        password = Label(pgstudent, text="Password").grid(row=3, column=2)
                        rollnumber = Label(pgstudent, text="RollNumber").grid(row=4, column=2)
                        year = Label(pgstudent, text="Year").grid(row=5, column=2)
                        cg = Label(pgstudent, text="CGPA").grid(row=6, column=2)


                        namevalue = StringVar()
                        uservalue = StringVar()
                        passvalue = StringVar()
                        rollvalue = StringVar()
                        yearvalue = StringVar()
                        cgvalue = StringVar()


                        nameentry = Entry(pgstudent, textvariable=namevalue).grid(row=1, column=3)
                        userentry = Entry(pgstudent, textvariable=uservalue).grid(row=2, column=3)
                        passentry = Entry(pgstudent, textvariable=passvalue).grid(row=3, column=3)
                        rollentry = Entry(pgstudent, textvariable=rollvalue).grid(row=4, column=3)
                        yearentry = Entry(pgstudent, textvariable=yearvalue).grid(row=5, column=3)
                        cgentry = Entry(pgstudent, textvariable=cgvalue).grid(row=6, column=3)


                        new_pg = pg_object(namevalue.get(),uservalue.get(),passvalue.get(),rollvalue.get(),yearvalue.get(),cgvalue.get())
                        #pg_lst.append(new_pg)
                        new_user = user_object(uservalue.get(),passvalue.get(),"pg_student")
                        #user_lst.append(new_user)

                        Button(pgstudent,text="Submit",command = check_password).grid(row=10, column=3)
                        #Button(text="Login",command = login).grid(row=7, column=4)
                        #tmsg.showinfo("result","hi")

                        pgstudent.mainloop()


                        
        #signup = Tk()
        signup.geometry("644x344")
        global typevar
        typevar = IntVar()
        #typevar.set("Radio")
        Label(signup, text = "Select the type of user.").grid(row=0, column=3)
        Radio = Radiobutton(signup, text="Teacher", variable=typevar, value=1).grid(row=1, column=3)
        Radio = Radiobutton(signup, text="UG Student", variable=typevar, value=2).grid(row=2, column=3)
        Radio = Radiobutton(signup, text="PG Student", variable=typevar, value=3).grid(row=3, column=3)
        Button(signup,text="Submit", command = order).grid(row=4, column=3)
       

        signup.mainloop()

                   
    
##########################################################################################################
    

Label(root, text="Enter user details").grid(row=0, column=3)


userid = Label(root, text="UserID (email)")
password = Label(root, text="Password")


userid.grid(row=1, column=2)
password.grid(row=2, column=2)

 
uservalue = StringVar()
passvalue = StringVar()


userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)


userentry.grid(row=1, column=3)
passentry.grid(row=2, column=3)

Button(text="Signup", command = signup_).grid(row=7, column=3)
