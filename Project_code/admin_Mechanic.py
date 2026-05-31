
import tkinter as tk
import User_services as Us
import os 
import admin_menu as Am
class admin_Mechanic:

    def __init__ (self,root):
      self.root=root
      self.Admin_M_frame=tk.Frame(self.root,bg="black")
      self.Admin_M_frame.pack(fill="x")
      self.button_exit=tk.Button(self.Admin_M_frame,text="Exit",command= root.destroy,font="bold",bg="red",fg="white",width=5,height=1)
      self.button_exit.pack(side="left",pady=2,padx=5)
      self.button_back=tk.Button(self.Admin_M_frame,text="Back",command= self.go_admin_menu,font="bold",bg="blue",fg="white",width=5,height=1)
      self.button_back.pack(side="left",pady=2,padx=5)
      self.Admin_M_label_1=tk.Label(self.Admin_M_frame,text="Mechanic Clock-In",fg="white",bg="black",font=("bold",20))
      self.Admin_M_label_1.pack(side="left",padx=5,pady=10)
      self.result_clock_in = Us.Mechanic_clock_in()
      self.all_mechanics_clock_in_print()

    def all_mechanics_clock_in_print(self):
       for returnitems in self.result_clock_in:
        self.Admin_M_frame=tk.Frame(self.root,bg="black")
        self.Admin_M_frame.pack(fill="x")
        self.Admin_M_label=tk.Label(self.Admin_M_frame,text=f"Mechanic:{returnitems}",fg="red",bg="black",font=("bold",14))
        self.Admin_M_label.pack(side="left",padx=100,pady=2)
    
    def go_admin_menu(self):
       for widget in self.root.winfo_children(): #katastrefei ola ta frames ean ekana pack.forget tha xexnouse mono to teleytaio frame 
          widget.destroy()
       Am.admin_menu(self.root)
    
    