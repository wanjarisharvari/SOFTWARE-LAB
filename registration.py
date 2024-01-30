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


''' creation of various objects of user teacher ug and pg which when called directly appends the list of attributes 
to the respective lists '''
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
            
'''the signup function which is called when the user click on sign up from the main page it first askes the user to 
select the type of user the selection of the type of user is done by radio buttons which changes the value of 
variable that decides the type of user and then takes the user to the registration page of the particular type of user '''

def signup_():

        signup = Toplevel(root)
        signup.title("Signup")
        def order():

                ''' check password function  to check if the password is correctly entered and also if the userid 
                is a gmail or not''' 

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

                '''if radio button value is 1 it is teacher this page takes userdetails checks userid and password
                a userobject and teacher object is called which stores the data in list and after the clik of check
                 button function to check password id called '''   
                     
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

                            new_user = user_object(uservalue.get(),passvalue.get(),"teacher")
                            #print(teacher_lst)
                        #user_lst.append(new_user)
                        

                        Button(teacher,text="Submit",command=lambda: [check_password(), submit_form()]).grid(row=10, column=3)
                        

                        teacher.mainloop()

                ''' similar things happen if the radio button value id 2 but entry is taken for ug '''

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

                ''' similar things happen if the radio button value id 2 but entry is taken for pg '''
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

        ''' initial signup page to select the type of user using radio buttons '''
                        
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


'''login function that check for th userid enterd and then finds the user id from the user_lst and shows messege id user is not find
after login the user is shown his details and can then delete or update his details'''        
def login_():
    login = Toplevel(root)
    login.title("Login")
    
    user_id = uservalue.get()
    user_password = passvalue.get()

    '''delet function to fins the user using userid in user lst and the particular list and them delet the row from the list'''
    
    def delete_teacher():
        for i in range (len(teacher_lst)) :
                    if(teacher_lst[i][1] == user_id):
                         teacher_lst.remove(teacher_lst[i])

        for i in range (len(user_lst)) :
                    if(user_lst[i][1] == user_id):
                         user_lst.remove(user_lst[i])
        tmsg.showinfo("result","Delete Successfully!")
            
    
    def delete_ug():
        for i in range (len(ug_lst)) :
                    if(ug_lst[i][1] == user_id):
                         ug_lst.remove(ug_lst[i])

        for i in range (len(user_lst)) :
                    if(user_lst[i][1] == user_id):
                         user_lst.remove(user_lst[i])
        tmsg.showinfo("result","Delete Successfully!")
    
    def delete_pg():
        for i in range (len(pg_lst)) :
                    if(pg_lst[i][1] == user_id):
                         pg_lst.remove(pg_lst[i])
        for i in range (len(user_lst)) :
                    if(user_lst[i][1] == user_id):
                         user_lst.remove(user_lst[i])
        tmsg.showinfo("result","Delete Successfully!")
    
    def update():
         tmsg.showinfo("result","Update Function not available!, Delete the current user and Sign up again")


    def update_teacher():
          
                        teacher = Toplevel(login)
                        teacher.title("Teacher")
                        teacher.geometry("644x344")
                        Label(teacher, text="Enter user details").grid(row=0, column=3)


                        name = Label(teacher, text="Name").grid(row=1, column=2)
                                               

                        namevalue = StringVar()
                    
                        nameentry = Entry(teacher, textvariable=namevalue).grid(row=1, column=3)              

                        new_teacher = teacher_object(namevalue.get(),user_id,user_password)
                      
                        new_user = user_object(user_id,user_password,"teacher")

                        for i in range (len(teacher_lst)) :
                            if(teacher_lst[i][1] == user_id):
                                teacher_lst.remove(teacher_lst[i])

                        for i in range (len(user_lst)) :
                            if(user_lst[i][1] == user_id):
                                user_lst.remove(user_lst[i])
                                 

                        Button(teacher,text="Submit").grid(row=10, column=3)
                       
                        teacher.mainloop()

    def ug_update():
                        ugstudent = Toplevel(login)
                        ugstudent.title("Ug Student")
                        ugstudent.geometry("644x344")
                        Label(ugstudent, text="Enter user details").grid(row=0, column=3)


                        name = Label(ugstudent, text="Name").grid(row=1, column=2)
                        #userid = Label(ugstudent, text="UserID (email)").grid(row=2, column=2)
                        #password = Label(ugstudent, text="Password").grid(row=3, column=2)
                        rollnumber = Label(ugstudent, text="RollNumber").grid(row=4, column=2)
                        year = Label(ugstudent, text="Year").grid(row=5, column=2)
                        cg = Label(ugstudent, text="CGPA").grid(row=6, column=2)


                        namevalue = StringVar()
                        #uservalue = StringVar()
                        #passvalue = StringVar()
                        rollvalue = StringVar()
                        yearvalue = StringVar()
                        cgvalue = StringVar()


                        nameentry = Entry(ugstudent, textvariable=namevalue).grid(row=1, column=3)
                        #userentry = Entry(ugstudent, textvariable=uservalue).grid(row=2, column=3)
                        #passentry = Entry(ugstudent, textvariable=passvalue).grid(row=3, column=3)
                        rollentry = Entry(ugstudent, textvariable=rollvalue).grid(row=4, column=3)
                        yearentry = Entry(ugstudent, textvariable=yearvalue).grid(row=5, column=3)
                        cgentry = Entry(ugstudent, textvariable=cgvalue).grid(row=6, column=3)


                        new_ug = ug_object(namevalue.get(),user_id,user_password,rollvalue.get(),yearvalue.get(),cgvalue.get())
                        #ug_lst.append(new_ug)
                        new_user = user_object(uservalue.get(),passvalue.get(),"ug_student")
                        #user_lst.append(new_user)

                        for i in range (len(ug_lst)) :
                            if(ug_lst[i][1] == user_id):
                                ug_lst.remove(ug_lst[i])

                        for i in range (len(user_lst)) :
                            if(user_lst[i][1] == user_id):
                                user_lst.remove(user_lst[i])


                        Button(ugstudent,text="Submit").grid(row=10, column=3)
                        #Button(text="Login",command = login).grid(row=7, column=4)
                        #tmsg.showinfo("result","hi")

                        ugstudent.mainloop()   

    def pg_update():
                        pgstudent = Toplevel(login)
                        pgstudent.title("Ug Student")
                        pgstudent.geometry("644x344")
                        Label(pgstudent, text="Enter user details").grid(row=0, column=3)


                        name = Label(pgstudent, text="Name").grid(row=1, column=2)
                        #userid = Label(ugstudent, text="UserID (email)").grid(row=2, column=2)
                        #password = Label(ugstudent, text="Password").grid(row=3, column=2)
                        rollnumber = Label(pgstudent, text="RollNumber").grid(row=4, column=2)
                        year = Label(pgstudent, text="Year").grid(row=5, column=2)
                        cg = Label(pgstudent, text="CGPA").grid(row=6, column=2)


                        namevalue = StringVar()
                        #uservalue = StringVar()
                        #passvalue = StringVar()
                        rollvalue = StringVar()
                        yearvalue = StringVar()
                        cgvalue = StringVar()


                        nameentry = Entry(pgstudent, textvariable=namevalue).grid(row=1, column=3)
                        #userentry = Entry(ugstudent, textvariable=uservalue).grid(row=2, column=3)
                        #passentry = Entry(ugstudent, textvariable=passvalue).grid(row=3, column=3)
                        rollentry = Entry(pgstudent, textvariable=rollvalue).grid(row=4, column=3)
                        yearentry = Entry(pgstudent, textvariable=yearvalue).grid(row=5, column=3)
                        cgentry = Entry(pgstudent, textvariable=cgvalue).grid(row=6, column=3)


                        new_ug = ug_object(namevalue.get(),user_id,user_password,rollvalue.get(),yearvalue.get(),cgvalue.get())
                        #ug_lst.append(new_ug)
                        new_user = user_object(uservalue.get(),passvalue.get(),"ug_student")
                        #user_lst.append(new_user)

                        for i in range (len(pg_lst)) :
                            if(pg_lst[i][1] == user_id):
                                pg_lst.remove(pg_lst[i])

                        for i in range (len(user_lst)) :
                            if(user_lst[i][1] == user_id):
                                user_lst.remove(user_lst[i])


                        Button(pgstudent,text="Submit").grid(row=10, column=3)
                        #Button(text="Login",command = login).grid(row=7, column=4)
                        #tmsg.showinfo("result","hi")

                        pgstudent.mainloop()  


    ''' finding of the user from user id and then showing the dtails of the user after fetching the details from the 
    particular list '''

    if(any(user_lst[i][0] == user_id for i in range(len(user_lst)))):
        
        for i in range (len(user_lst)):
            if user_lst[i][0]== user_id and user_lst[i][1] == user_password :
                if(user_lst[i][2] == "teacher"):
                    for i in range (len(teacher_lst)) :
                        if(teacher_lst[i][1] == user_id):
                            show = Toplevel(login)
                            show.geometry("644x344")
                            Label(show, text = "User ID:").grid(row=2 , column = 1)
                            userid = Label(show, text=teacher_lst[i][1]).grid(row=2, column=3)
                            Label(show, text = "Name:").grid(row=3 , column = 1)
                            name = Label(show, text=teacher_lst[i][0]).grid(row=3, column=2)
                            Label(show, text = "Type:").grid(row=4 , column = 1)
                            Label(show, text = "Teacher").grid(row=4 , column = 2)
                            #password = Label(show, text=teacher_lst[i][2]).grid(row=3, column=2) 

                            Button(show,text="Update",command = update_teacher).grid(row=5, column=3)
                            Button(show,text="Delete", command = delete_teacher).grid(row=5, column=4)

                            show.mainloop()
                if(user_lst[i][2] == "ug_student"):
                    for i in range (len(ug_lst)) :
                        if(ug_lst[i][1] == user_id):
                            show = Toplevel(login)
                            show.geometry("644x344")
                            userid = Label(show, text=ug_lst[i][1]).grid(row=1, column=2)
                            name = Label(show, text=ug_lst[i][0]).grid(row=2, column=2)
                            password = Label(show, text=ug_lst[i][2]).grid(row=3, column=2) 
                            rollnumber = Label(show, text=ug_lst[i][3]).grid(row=4, column=2)
                            year = Label(show, text=ug_lst[i][4]).grid(row=5, column=2)
                            cg = Label(show, text=ug_lst[i][5]).grid(row=6, column=2)
                            course = Label(show, text=ug_lst[i][6]).grid(row=7, column=2)

                            Button(show,text="Update",command = ug_update).grid(row=8, column=3)
                            Button(show,text="Delete",command = delete_ug).grid(row=8, column=4)

                            show.mainloop()

                if(user_lst[i][2] == "pg_student"):
                    for i in range (len(pg_lst)) :
                        if(pg_lst[i][1] == user_id):
                            show = Toplevel(login)
                            show.geometry("644x344")
                            userid = Label(show, text=pg_lst[i][1]).grid(row=1, column=2)
                            name = Label(show, text=pg_lst[i][0]).grid(row=2, column=2)
                            password = Label(show, text=pg_lst[i][2]).grid(row=3, column=2) 
                            rollnumber = Label(show, text=pg_lst[i][3]).grid(row=4, column=2)
                            year = Label(show, text=pg_lst[i][4]).grid(row=5, column=2)
                            cg = Label(show, text=pg_lst[i][5]).grid(row=6, column=2)
                            course = Label(show, text=pg_lst[i][6]).grid(row=7, column=2)

                            Button(show,text="Update",command = pg_update).grid(row=8, column=3)
                            Button(show,text="Delete",command = delete_pg).grid(row=8, column=4)

                            show.mainloop()



    else : 
           tmsg.showinfo("result","user not registered!")

    login.mainloop()                              
        
    
    
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
Button(text="Login",command = login_).grid(row=7, column = 4)
