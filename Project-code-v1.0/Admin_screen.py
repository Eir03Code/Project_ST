
import tkinter as tk
import User_services as Us
import os 
import admin_menu as Am
class Admin:

    def __init__ (self,root):
      self.root=root
      self.Admin_frame=tk.Frame(self.root,bg="black")
      self.Admin_frame.pack(fill="x")
      self.button_exit=tk.Button(self.Admin_frame,text="Exit",command= root.destroy,font="bold",bg="red",fg="white",width=5,height=1)
      self.button_exit.pack(side="left",pady=2,padx=5)
      self.button_back=tk.Button(self.Admin_frame,text="Back",command= self.go_admin_menu,font="bold",bg="blue",fg="white",width=5,height=1)
      self.button_back.pack(side="left",pady=2,padx=5)
      self.Admin_label_1=tk.Label(self.Admin_frame,text="Customer Data",fg="white",bg="black",font=("bold",20))
      self.Admin_label_1.pack(side="left",padx=5,pady=2)
      self.button_metrics=tk.Button(self.Admin_frame,text="Statistics",command= self.statistics ,font="bold",bg="green",fg="white",width=20,height=1)
      self.button_metrics.pack(side="right",padx=20)
      self.result_data = Us.customers_pdf()
      self.all_customers_print()

    def open_pdf(self,filename):
        os.startfile(filename)

    def all_customers_print(self):
       for details,filename in self.result_data:
        self.Admin_frame=tk.Frame(self.root,bg="black")
        self.Admin_frame.pack(fill="x")
        self.Admin_label=tk.Label(self.Admin_frame,text="",fg="red",bg="black",font=("bold",14))
        self.button_c=tk.Button(self.Admin_frame,text="Feedback",font="bold" ,bg="gray",fg="black",width=20,height=1)
        self.Admin_label.config(text=f"{details}")
        self.button_c.config(command=lambda: self.open_pdf(filename))
        self.Admin_label.pack(side="left",padx=100,pady=2)
        self.button_c.pack(side="right",padx=20,pady=2) 
        
    def statistics(self):
      pdf= Us.Metrics_pdf()
      os.startfile(pdf)

    def go_admin_menu(self):
       for widget in self.root.winfo_children():
          widget.destroy()
       Am.admin_menu(self.root)