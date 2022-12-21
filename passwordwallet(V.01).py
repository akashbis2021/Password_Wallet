#!/usr/bin/env python3
from tkinter import*
import tkinter as tk
from tkinter import messagebox
import random
import os
from tkinter import scrolledtext

wallet=tk.Tk()
wallet.title("login_page")
wallet.geometry('700x300')



#Login-page content............
headerlogin=tk.Label(wallet,text="LOGIN")
username_login=tk.Label(wallet,text="Username")
password_login=tk.Label(wallet,text="Password")
#Entry for Login page.............
login_username_entry=tk.Entry(wallet,width=30)
login_password_entry=tk.Entry(wallet,width=30)

                      
                          
#Login button linking..........
def login():
    username_login=login_username_entry.get()
    password_login=login_password_entry.get()
   

    if not os.path.exists(".loginlog"):
     tk.Label(wallet, text="Error: Login Credentials not found!!").place(x=230,y=250)
     return
    
    with open('.loginlog') as f1:
     contents=f1.read()   

    login_username, login_password = contents.split()

    if username_login == login_username and password_login==login_password:
        wallet.destroy() 
    else:
        messagebox.showerror(title="Error",message="Not match")    

                              #==============X==============#
    
    # BACKEND CONTENT
    
    #linking with Main content...........
    login_page=Tk()
    login_page.title('Password-Wallet')
    login_page.maxsize(700,300)
    login_page.minsize(700,300)    
    def main_linking():
        website=weblink.get()
        email_id=email.get()
        password=password_entry.get()
        
    #Read/Write/checking.............
        
        if len(website)==0 or len(password)==0:
            messagebox.showerror(title="Error",message="Feilds are empty") 
        else:
           checking=messagebox.askokcancel(title=website,message=f"Details\nwebsite:{website}\n email:{email_id}\npassword:{password}\n\n"f"Did you want to save deatils")
    
           if checking:
            with open("pass","a") as f:
                f.write(f'website:{website} || Email:{email_id} || Password:{password}\n')
            weblink.delete(0,END)
            password_entry.delete(0,END)
            email.delete(0,END)
    
    #Genratepass.........
    def genratepass():
        lowcase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","w","u","v","x","y","z"]
    
        upcase=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","W","U","V","X","Y","Z"]
    
        numbers=["0","1","2","3","4","5","6","7","8","9"]
    
        symbolic=["!","@","#","$","%","^","&","*","(",")","-","+",":","/","<",">","?","."]
    
        rangenumbers=random.randint(2, 5)
        rangesymbolic=random.randint(2, 4)
        rangeupcase=random.randint(8, 10)
        rangelowcase=random.randint(8,10)
    
        passlist =[random.choice(lowcase) for _ in range(rangelowcase)]
        passlist +=[random.choice(upcase) for _ in range(rangeupcase)]
        passlist +=[random.choice(numbers) for _ in range(rangenumbers)]
        passlist +=[random.choice(symbolic) for _ in range(rangesymbolic)]
    
    
        random.shuffle(passlist)
    
        password=""
        for char in passlist:
            password+=char
    
        password_entry.insert(END,password)
        password_entry.clipboard_clear()
        password_entry.clipboard_append(password)
    
    def show_entry():
        window = tk.Tk()
        window.title("File Viewer")
        window.geometry('700x300')
        
        text_widget = scrolledtext.ScrolledText(window)
        text_widget.pack()
    
        with open("pass", "r") as f:
         contents = f.read()
        text_widget.insert(tk.END, contents)
        window.mainloop()
    
    #Labeling for main content...........
    header=Label(login_page,text="Password-Wallet")
    header.pack()
    header.place(x=300,y=10)
    website=Label(login_page,text="Weblink (https/http)")
    website.pack()
    website.place(x=80,y=65)
    email_id=Label(login_page,text="email/username:")
    email_id.pack()
    email_id.place(x=80,y=95)
    password=Label(login_page,text="password:")
    password.pack()
    password.place(x=80,y=125)
    
    #entryboxes for main content:......
    
    weblink=Entry(login_page,width=30)
    weblink.pack()
    weblink.place(x=225,y=70)
    
    email=Entry(login_page,width=30)
    email.pack()
    email.place(x=225,y=99)
    
    password_entry=Entry(login_page,width=30)
    password_entry.pack()
    password_entry.place(x=225,y=125)
    
    #buttons for main contents..........
    Genpass_btn=Button(login_page,text="Random Password",width=20,command=genratepass)
    Genpass_btn.pack()
    Genpass_btn.place(x=500,y=50)
    
    add_btn=Button(login_page,text="Add",width=10,command=main_linking)
    add_btn.pack()
    add_btn.place(x=225,y=200)
    
    all_details=Button(login_page,text="All-Entries",width=10,command=show_entry)
    all_details.pack()
    all_details.place(x=360,y=200)
    
    
    login_page.mainloop()
    

                             #============X=============#

# Register button linking...........
def register():
   username_login=login_username_entry.get()
   password_login=login_password_entry.get()
   
   if len(username_login)==0 or len(password_login)==0:
         messagebox.showerror(title="Error",message="Feilds are empty") 
   else:
          checking1=messagebox.askokcancel(title="Login-details",message=f"Details\nusername:{username_login}\npassword:{password_login}\n\n"f"Did you want to save deatils")

   if checking1:
        with open(".loginlog","a") as f2:
         f2.write(f'{username_login} {password_login}')
         login_username_entry.delete(0,END)
         login_password_entry.delete(0,END)

def reset():
    login_file=".loginlog"
    if os.path.exists(login_file):
        os.remove(login_file)
        tk.Label(wallet, text="Login-Credentails-Reset",width=50).place(x=145,y=255)
    else:
        tk.Label(wallet, text="Error: Not-found",width=50).place(x=145,y=255)
                    

#Button for Login page............
login_btn=tk.Button(wallet,text="Sign-In",width=6,command=login)
register_btn=tk.Button(wallet,text="Register",width=6,command=register)
reset_btn=tk.Button(wallet,text="Forgot-Password ?",bd=0,width=12,command=reset)
headerlogin.pack()
headerlogin.place(x=320,y=15)
username_login.pack()
username_login.place(x=225,y=75)
password_login.pack()
password_login.place(x=225,y=125)
login_username_entry.pack()
login_username_entry.place(x=225,y=99)
login_password_entry.pack()
login_password_entry.place(x=225,y=150)
login_btn.pack()
login_btn.place(x=250,y=215)
register_btn.pack()
register_btn.place(x=360,y=215)
reset_btn.pack()
reset_btn.place(x=226,y=175)
wallet.mainloop()
