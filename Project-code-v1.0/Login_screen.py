
import tkinter as tk
from Menu_screen import Menu
import Admin_screen as As
import Mechanic_screen as M
import admin_menu as Am

class Login:     
   
   def __init__ (self,root):  
      
      self.root=root
      self.root.title("Garage")
      self.root.iconbitmap("icon.ico")
      self.root.geometry("700x400+400+200")
      self.root.resizable(False,False)

      self.frame=tk.Frame(self.root,bg="black")
      self.frame.pack(expand=True,anchor="center")

      self.email_connection=tk.Label(self.frame,text="E-mail",fg="white",bg="black",font="bold")
      self.email_connection.pack(side="top")
      self.Entry1=tk.Entry(self.frame,width=30)
      self.Entry1.pack(side="top")
      
    

      self.paswd_connection=tk.Label(self.frame,text="Password",fg="white",bg="black",font="bold")
      self.paswd_connection.pack(side="top")
      self.Entry2=tk.Entry(self.frame,width=30,show="*")
      self.Entry2.pack(side="top") 
      

      
      self.button=tk.Button(self.frame,text="Login",command= self.login_info,font="bold",bg="gray",fg="black",width=6,height=1)
      self.button.pack(side="left",pady=20,padx=10) 

      self.button_exit=tk.Button(self.frame,text="Exit",command= root.destroy,font="bold",bg="red",fg="white",width=6,height=1)
      self.button_exit.pack(side="left",padx=5)

      self.root.configure(bg="black")

   def login_info (self):
         email_check=self.Entry1.get()
         password_check=self.Entry2.get()
         import User_services as Us
         result,flag = Us.check(email_check,password_check)
         if result==1 and flag=="C":
             self.frame.pack_forget()
             Menu(self.root)
         elif result==1 and flag=="A":
            self.frame.pack_forget()
            Am.admin_menu(self.root)
         elif result==1 and flag=="M":
            self.frame.pack_forget()
            M.Mechanic(self.root)

   

  

  