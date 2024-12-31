from tkinter import *
from tkinter import messagebox
import re
import json

#validating the pssword at the time of entery
def validate_11(char, entry_text):
    is_valid = validity(entry_text)
    if is_valid=='Valid':
        texts.config(fg="green")
    else:
        texts.config(fg="red")
    tex.set(is_valid)
    texts.grid(row=5,column=1,columnspan=2)
    return True

#Function verifying the valid input in Name and Hall 
def validate_input(char):
    # Check if the entered character is an alphabet
    if char.isalpha() or char == "":
        return True
    else:
        messagebox.showerror("Error","Name can't conatin symbols or numbers")

#Function verifying the valid input in Name and Hall 
def on_validate(P):
    # P is the input being added to the Entry widget
    if not validate_input(P):
        return False
    return True

#function asking for the confirmation of closing the page
def onclose():
    result = messagebox.askquestion("Confirmation","Do you really want to quit")
    if result == "yes":
        root.destroy()

#class Defined for the person
class Person:
    def __init__(self,firstname,lastname,username,password,department):
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password
        self.department=department
        self.wrong=0

#Class Defined for Teacher inheriting from Person
class Teachers(Person):
    def __init__(self,firstname,lastname,username,password,department,area):
        Person.__init__(self,firstname,lastname,username,password,department)
        self.area=area
        self.type=" Teacher "

#Class Defined for Students inheriting from Person
class Student(Person):
    def __init__(self,firstname,lastname,username,password,department,hall,roll):
        Person.__init__(self,firstname,lastname,username,password,department)
        self.hall=hall  
        self.roll=roll

#Class Defined for UG Students inheriting from Student
class UG_Student(Student):
    def __init__(self,firstname,lastname,username,password,department,hall,roll):
        Student.__init__(self,firstname,lastname,username,password,department,hall,roll)
        self.type="UG Student"

#Class Defined for PG Students inheriting from Student
class PG_Student(Student):
    def __init__(self,firstname,lastname,username,password,department,hall,roll,area):
        Student.__init__(self,firstname,lastname,username,password,department,hall,roll)
        self.area=area
        self.type="PG Student"

#deregestering the member from text file 
def dereg(user):
    response=messagebox.askquestion("Confirmation", "Are you sure you wan't to deregister?")
    if response == 'yes': 
        with open('file.txt', 'w') as json_file: 
            for auser in totallist:
                if not auser["username"] == user :  
                    str_json=json.dumps(auser)  
                    json_file.write(str_json+'\n')
        messagebox.showinfo("Confirmation", "You have Deregistered Sucessfully") 
        main()

#updating the details of user in the file
def doneupdation(auser,pas,repas,update,user):
    if(validity(pas)=='Valid' and pas==repas):
        if(user in uname and user!=auser["username"]):
            messagebox.showerror("error","sorry for the inconvinience the user name is already in use")
        else:
            uname.remove(auser["username"])
            totallist.remove(auser)
            check(auser["type"])
            with open('file.txt', 'w') as json_file: 
                for buser in totallist:
                    str_json=json.dumps(buser)  
                    json_file.write(str_json+'\n')    
            messagebox.showinfo("Confirmation", "Your information is updated sucessfully") 
    elif(validity(pas)=='Valid'):
        messagebox.showerror("error","password not matches with retyped password")
    else:
        error = validity(pas)
        messagebox.showerror("error",error)   
    nope.grid_forget()  
    update.grid_forget()
    update.grid(row=50,column=0,padx=10,pady=10,sticky=EW,columnspan=3)



#UI for the updation page of a user
def upto(auser):
    for i in root.grid_slaves():
        i.grid_forget()
    global halll,rol,areaof,FirstName,LastName,username,password,repassword,dept,tex,nope
    info =Label(root,text="You want to Update your Profile",font=("Times", 18 ,"bold"))
    fname = Label(root,text="First Name :")
    lname = Label(root,text="Last Name : ")
    user = Label(root,text="Username:")
    passw = Label(root,text="Password:")
    repassw = Label(root,text="Reenter Password:")
    Depart = Label(root,text="Department: ")
    FirstName = Entry(root,width=18,border=5,validate="key", validatecommand=(vcmd, "%P"))
    FirstName.insert(0,auser["firstname"])
    LastName = Entry(root,width=18,border=5,validate="key", validatecommand=(vcmd, "%P"))
    LastName.insert(0,auser["lastname"])
    username = Entry(root,width=18,border=5)
    username.insert(0,auser["username"])
    Checkbutton1 = IntVar() 
    Button1 = Checkbutton(root,variable = Checkbutton1,onvalue = 1,offvalue = 0,height = 2,width = 2,command=lambda: Unmask(Button1,Checkbutton1,password)) 
    password = Entry(root,width=12,border=5,show='*')
    password.insert(0,auser["password"]) 
    Checkbutton2 = IntVar() 
    Button2 = Checkbutton(root,variable = Checkbutton2,onvalue = 1,offvalue = 0,height = 2,width = 2,command=lambda: Unmask(Button2,Checkbutton2,repassword)) 
    repassword= Entry(root,width=12,border=5,show='*')
    repassword.insert(0,auser["password"]) 
    dept = Entry(root,width=18,border=5)
    dept.insert(0,auser["department"]) 
    nope = Button(root,text="Back", command =loggedinpage,fg="white", bg="blue")
    update = Button(root,text="Update", command = lambda : doneupdation(auser,password.get(),repassword.get(),update,username.get()) ,fg="white", bg="blue")
    if(auser["type"]==" Teacher "):
        area= Label(root,text="Area of Research:")
        area.grid(row=8,column=0)
        areaof = Entry(root,width=18,border=5)
        areaof.grid(row=8,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
        areaof.insert(0,auser["area"])  
    if(auser["type"]=="UG Student"):
        roll= Label(root,text="Roll Number:")
        roll.grid(row=8,column=0)
        rol = Entry(root,width=18,border=5)
        rol.grid(row=8,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
        rol.insert(0,auser["roll"])  
        hall= Label(root,text="Hall of residence")
        hall.grid(row=9,column=0)
        halll = Entry(root,width=18,border=5,validate="key", validatecommand=(vcmd, "%P"))
        halll.grid(row=9,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
        halll.insert(0,auser["hall"])  
    if(auser["type"]=="PG Student"):
        roll= Label(root,text="Roll Number:")
        roll.grid(row=8,column=0)
        rol = Entry(root,width=18,border=5)
        rol.grid(row=8,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
        rol.insert(0,auser["roll"])  
        hall= Label(root,text="Hall of residence")
        hall.grid(row=9,column=0)
        halll = Entry(root,width=18,border=5,validate="key", validatecommand=(vcmd, "%P"))
        halll.grid(row=9,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
        halll.insert(0,auser["hall"])  
        area= Label(root,text="Area of Research:")
        area.grid(row=10,column=0)
        areaof = Entry(root,width=18,border=5)
        areaof.grid(row=10,column=1,padx=10,pady=10,sticky=EW)
        areaof.insert(0,auser["area"])  
    info.grid(row=0,column=0,columnspan=3,padx=2,pady=2,sticky=EW)
    fname.grid(row=1,column=0,padx=10,pady=10,sticky=EW)
    FirstName.grid(row=1,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
    lname.grid(row=2,column=0,padx=10,pady=10,sticky=EW)
    LastName.grid(row=2,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
    user.grid(row=3,column=0,sticky=EW)
    username.grid(row=3,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
    passw.grid(row=4,column=0,sticky=EW) 
    password.grid(row=4,column=1,padx=10,pady=10,sticky=EW)
    Button1.grid(row=4,column=2)
    Button2.grid(row=6,column=2)
    repassw.grid(row=6,column=0,sticky=EW) 
    repassword.grid(row=6,column=1,padx=10,pady=10,sticky=EW)
    Depart.grid(row=7,column=0,sticky=EW) 
    dept.grid(row=7,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
    update.grid(row=50,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
    nope.grid(row=50,column=0,padx=10,pady=10,sticky=EW)

#UI of the Logged in Page
def loggedinpage():
    pas=password.get()
    user=username.get()
    for auser in totallist:
        if(auser["username"]==user and auser["password"]==pas):    
            for i in root.grid_slaves():
                i.grid_forget()
            buser=auser
            hellow = Label(root,text="Hello "+buser["firstname"]+" "+buser["lastname"],font=("MSSerif", 22 ,"bold"))
            info =Label(root,text="You have entered as a "+ buser["type"],font=("Times", 18 ,"bold"))
            fname = Label(root,text="First Name : "+buser["firstname"])
            lname = Label(root,text="Last Name : "+buser["lastname"])
            Depart = Label(root,text="Department: "+buser["department"])
            update = Button(root,text="Update",command=lambda: upto(buser),fg="white",bg="blue",padx=5,pady=5)
            deregister = Button(root,text="De register",command=lambda : dereg(user),fg="white",bg="red",padx=5,pady=5)
            Logout = Button(root,text="Log out",command=login,fg="white",bg="red",pady=5,padx=5)
            if(auser["type"]==" Teacher "):
                area= Label(root,text="Area of Research:"+buser["area"])
                area.grid(row=8,column=0,padx=10,pady=10,sticky=EW,columnspan=3)
            if(auser["type"]=="UG Student"):
                roll= Label(root,text="Roll Number: "+buser["roll"])
                roll.grid(row=8,column=0,padx=10,pady=10,sticky=EW,columnspan=3)
                hall= Label(root,text="Hall of residence: "+buser["hall"])
                hall.grid(row=9,column=0,padx=10,pady=10,sticky=EW,columnspan=3)
            if(auser["type"]=="PG Student"):
                roll= Label(root,text="Roll Number: "+ buser["roll"])
                roll.grid(row=8,column=0,padx=10,pady=10,sticky=EW,columnspan=3)
                hall= Label(root,text="Hall of residence : "+buser["hall"])
                hall.grid(row=9,column=0,padx=10,pady=10,sticky=EW,columnspan=3)
                area= Label(root,text="Area of Research: " +buser["area"])
                area.grid(row=10,column=0,padx=10,pady=10,sticky=EW,columnspan=3)            
            hellow.grid(row=0,column=0,padx=10,pady=10,columnspan=3)
            info.grid(row=1,column=0,padx=2,pady=2,sticky=EW,columnspan=3)
            fname.grid(row=2,column=0,padx=10,pady=10,sticky=EW,columnspan=3)
            lname.grid(row=3,column=0,padx=10,pady=10,sticky=EW,columnspan=3)
            Depart.grid(row=4,column=0,padx=10,pady=10,sticky=EW,columnspan=3)
            Logout.grid(row=50,column=0,padx=10,pady=10,sticky=EW)
            deregister.grid(row=50,column=1,padx=10,pady=10,sticky=EW)
            update.grid(row=50,column=2,padx=10,pady=10,sticky=EW)
        else:
            pass

#checking the strength of the password            
def validity(password):
    flag = 'Valid'
    while True:
        if (len(password)<8 or len(password)>12):
            flag = 'length of password must be between 8 & 12. '
            break
        elif not re.search("[A-Z]", password):
            flag = 'password must contain atleast a capital Letter.'
            break
        elif not re.search("[0-9]", password):
            flag = 'password must contain atleast a Number.'
            break
        elif not re.search("[a-z]", password):
            flag = 'password must contain atleast a Small Letter.'
            break
        elif not re.search("[!@#$%&*]" , password):
            flag = 'password must contain atleast a Symbol.'
            break
        elif ' ' in password:
            flag = 'There should not be any space'
            break
        else :
            flag= 'Valid'
            break
    return flag

#function verifying that all credentials are in the right formate
def check(typed):
    pas=password.get()
    pas2=repassword.get()
    if(validity(pas)=='Valid' and pas==pas2):
        user=username.get()
        if user in uname:
            messagebox.showerror("error","Sorry for the inconvenience The Username is already Being Used please select diffrent Username.")
            return
        fname=FirstName.get()
        if(len(fname)==0):
            messagebox.showerror("error","First name can't be empty")  
            return    
        lname=LastName.get()
        if(len(lname)==0):
            messagebox.showerror("error","Last name can't be empty")
            return
        department=dept.get()
        if(len(department)==0):
            messagebox.showerror("error","department can't be empty")
            return
        if(typed==" Teacher "):
            area=areaof.get()
            if(len(area)==0):
                messagebox.showerror("error","Area of reserch can't be empty")
                return
            else:
                cla=Teachers(fname,lname,user,pas,department,area)
                str_json=json.dumps(cla.__dict__)
        elif(typed=="UG Student"):
            roll=rol.get()
            hall=halll.get()
            if(len(roll)==0):
                messagebox.showerror("error","Roll no. can't be empty")
            elif(len(hall)==0):
                messagebox.showerror("error","Hall field can't be empty")
            else:
                cla=UG_Student(fname,lname,user,pas,department,hall,roll)
                str_json=json.dumps(cla.__dict__)
        elif(typed=="PG Student"):
            roll=rol.get()
            hall=halll.get()
            area=areaof.get()
            if(len(roll)==0):
                messagebox.showerror("error","Roll no. can't be empty")
            elif(len(hall)==0):
                messagebox.showerror("error","Hall field can't be empty")
            elif(len(area)==0):
                messagebox.showerror("error","Area of reserch can't be empty")
            else:
                cla=PG_Student(fname,lname,user,pas,department,hall,roll,area)
                str_json=json.dumps(cla.__dict__)
        totallist.append(cla.__dict__) 
        uname.append(cla.__dict__["username"])   
        with open('file.txt', 'a') as json_file: 
            json_file.write(str_json+'\n')
        loggedinpage()
    if validity(pas)!='Valid':
        error = validity(pas)
        messagebox.showerror("error",error)
        return
    if pas!=pas2:
        messagebox.showerror("error","password won't match with reentered password")
        return

def Unmask(Button1,Checkbutton1,pas):
    if(Checkbutton1.get()==0):
        pas.config(show='*')
    else:
        pas.config(show='')

#Function for handelling the sign up action        
def signin1():
    for i in root.grid_slaves():
        i.grid_forget()
    
    if(clicked.get()=="       "):
        messagebox.showerror("error","please specify the answer")
        signin()
        return
    info =Label(root,text="You want to Sign Up as "+ clicked.get(),font=("Times", 18 ,"bold"))
    fname = Label(root,text="First Name :")
    lname = Label(root,text="Last Name : ")
    user = Label(root,text="Username:")
    passw = Label(root,text="Password:")
    Checkbutton1 = IntVar() 
    global FirstName,LastName,username,password,repassword,dept,halll,rol,areaof
    password = Entry(root,width=14,border=5,show='*',validate="key", validatecommand=(v_cmd, "%S","%P"))
    Button1 = Checkbutton(root,variable = Checkbutton1,onvalue = 1,offvalue = 0,height = 2,width = 2,command=lambda: Unmask(Button1,Checkbutton1,password)) 
    repassw = Label(root,text="Reenter Password:")
    Checkbutton2 = IntVar() 
    repassword= Entry(root,width=14,border=5,show='*')
    Button2 = Checkbutton(root,variable = Checkbutton2,onvalue = 1,offvalue = 0,height = 2,width = 2,command=lambda: Unmask(Button2,Checkbutton2,repassword)) 
    Depart = Label(root,text="Department: ")
    FirstName = Entry(root,width=18,border=5,validate="key", validatecommand=(vcmd, "%P"))
    LastName = Entry(root,width=18,border=5,validate="key", validatecommand=(vcmd, "%P"))
    username = Entry(root,width=18,border=5)
    dept = Entry(root,width=18,border=5)
    SignUp = Button(root,text="Sign Up", command = lambda: check(clicked.get()) ,fg="white", bg="blue")
    Back = Button(root,text="Back",command = signin,fg="white",bg="blue")
    if(clicked.get()==" Teacher "):
        area= Label(root,text="Area of Research:")
        area.grid(row=8,column=0)
        areaof = Entry(root,width=18,border=5)
        areaof.grid(row=8,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
    if(clicked.get()=="UG Student"):
        roll= Label(root,text="Roll Number:")
        roll.grid(row=8,column=0)
        rol = Entry(root,width=18,border=5)
        rol.grid(row=8,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
        hall= Label(root,text="Hall of residence")
        hall.grid(row=9,column=0)
        halll = Entry(root,width=18,border=5,validate="key", validatecommand=(vcmd, "%P"))
        halll.grid(row=9,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
    if(clicked.get()=="PG Student"):
        roll= Label(root,text="Roll Number:")
        roll.grid(row=8,column=0)
        rol = Entry(root,width=18,border=5)
        rol.grid(row=8,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
        hall= Label(root,text="Hall of residence")
        hall.grid(row=9,column=0)
        halll = Entry(root,width=18,border=5,validate="key", validatecommand=(vcmd, "%P"))
        halll.grid(row=9,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
        area= Label(root,text="Area of Research:")
        area.grid(row=10,column=0)
        areaof = Entry(root,width=18,border=5)
        areaof.grid(row=10,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
    global tex,texts
    tex = StringVar()
    texts=Label(root,textvariable=tex,fg="red")
    Button1.grid(row=4,column=2)
    Button2.grid(row=6,column=2)
    info.grid(row=0,column=0,columnspan=3,padx=2,pady=2,sticky=EW)
    fname.grid(row=1,column=0,padx=10,pady=10,sticky=EW)
    FirstName.grid(row=1,column=1,columnspan=2,padx=10,pady=10,sticky=EW)
    lname.grid(row=2,column=0,padx=10,pady=10,sticky=EW)
    LastName.grid(row=2,column=1,columnspan=2,padx=10,pady=10,sticky=EW)
    user.grid(row=3,column=0,sticky=EW)
    username.grid(row=3,column=1,columnspan=2,padx=10,pady=10,sticky=EW)
    passw.grid(row=4,column=0,sticky=EW) 
    password.grid(row=4,column=1,padx=10,sticky=EW)
    repassw.grid(row=6,column=0,sticky=EW) 
    repassword.grid(row=6,column=1,padx=10,sticky=EW)
    Depart.grid(row=7,column=0,sticky=EW) 
    dept.grid(row=7,column=1,columnspan=2,padx=10,pady=10,sticky=EW)
    SignUp.grid(row=50,column=1,columnspan=2,padx=10,pady=10,sticky=EW)
    Back.grid(row=50,column=0,padx=10,pady=10,sticky=EW)

#UI of the Sign up page
def signin():
    for i in root.grid_slaves():
        i.grid_forget()
    
    ques=Label(root,text="Sign Up as a/an :")
    cont = Button(root,text="continue", command = signin1 ,fg="white", bg="blue")
    Back = Button(root,text="Back",command = main,fg="white",bg="blue")
    type = [
    " Teacher ", 
    "UG Student", 
    "PG Student"
    ] 
    global clicked
    clicked = StringVar() 
    clicked.set("       ")
    drop = OptionMenu( root , clicked , *type ) 

    ques.grid(row=1,column=0,sticky=EW)
    drop.grid(row=1,column=1,sticky=EW)
    cont.grid(row=50,column=1,padx=10,pady=10,sticky=EW)
    Back.grid(row=50,column=0,padx=10,pady=10,sticky=EW)

#function that verify credentials during login
def verify():
    pas=password.get()
    user=username.get()    
    for auser in totallist:
        if(auser["username"]==user and auser["password"]==pas):
            loggedinpage()
            return
        elif(auser["username"]==user and auser["password"]!=pas):
            if(auser["wrong"]<2):
                messagebox.showinfo("info","The User name and Password do not match")
                auser["wrong"] = auser["wrong"]+1
                return
            elif(auser["wrong"]==2):
                messagebox.showinfo("info","Too many wrong attempts you have been deregisterd")
                with open('file.txt', 'w') as json_file: 
                    for buser in totallist:
                        if buser["username"] != user :  
                            str_json=json.dumps(buser)  
                            json_file.write(str_json+'\n')
                main()
                return
    messagebox.showinfo("info","User name does not exists")

# UI of the login page
def login():
    for i in root.grid_slaves():
        i.grid_forget()
    global username,password
    user= Label(root,text="Username:")
    username= Entry(root,width=15,border=5)
    passw= Label(root,text="Password:")
    password= Entry(root,width=12,border=5,show='*')
    Checkbutton1 = IntVar() 
    Button1 = Checkbutton(root,variable = Checkbutton1,onvalue = 1,offvalue = 0,height = 2,width = 2,command=lambda: Unmask(Button1,Checkbutton1,password)) 
    Login = Button(root,text="Log In",command=verify,fg="white",bg="blue")
    Back = Button(root,text="Back",command=main,fg="white",bg="blue")   
    Login.grid(row=50,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
    Back.grid(row=50,column=0,padx=5,pady=10,sticky=EW)
    user.grid(row=1,column=0,sticky=EW)
    Button1.grid(row=2,column=2)
    username.grid(row=1,column=1,padx=10,pady=10,sticky=EW,columnspan=2)
    passw.grid(row=2,column=0,sticky=EW)
    password.grid(row=2,column=1,padx=10,pady=10,sticky=EW)

#main Function initializing the application
def main():
    global totallist
    totallist = []
    global uname
    uname=[]
    #loading the information from the text file
    try:
        with open('file.txt', 'r') as json_file:
            lines = json_file.readlines()
            for line in lines:
                if line.strip():
                    try:
                        data = json.loads(line)
                        totallist.append(data)
                        uname.append(data["username"])
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON: {e}")
    except FileNotFoundError:
        print("File not found.")

    for i in root.grid_slaves():
        i.grid_forget()
    welco  = Label(root,text="Welcome!",padx=50,pady=20,font=("MSSerif", 22 ,"bold"))
    Signin = Button(root,text="Sign Up",command=signin,fg="white",bg="blue")
    Login = Button(root,text="Log In",command=login,fg="white",bg="blue")

    welco.grid(row=0,column=0,columnspan=2,sticky=EW)
    Signin.grid(row=50,column=0,padx=10,pady=10,sticky=EW)
    Login.grid(row=50,column=1,padx=10,pady=10,sticky=EW)

    root.mainloop()

root =Tk()
root.title("Welcome to the page")
root.protocol("WM_DELETE_WINDOW",onclose)
vcmd = root.register(on_validate)
v_cmd = root.register(validate_11)

main()