
import tkinter as tk
import Admin_screen as As
import admin_Mechanic as Am


class admin_menu:

   def __init__ (self,root):
      
      self.root=root
      self.A_Menu_frame=tk.Frame(self.root,bg="black")
      self.A_Menu_frame.pack(pady=50)
      self.A_Menu_label=tk.Label(self.A_Menu_frame,text="Admin Menu",fg="white",bg="black",font=("bold",20))
      self.A_Menu_label.pack(side="top",padx=10,pady=10)
      self.button2=tk.Button(self.A_Menu_frame,text="Αξιολογήσεις Πελατών",command= self.Costumers_reviews  ,font="bold",bg="gray",fg="black",width=20,height=1)
      self.button2.pack(side="top",pady=10) 
      self.button2=tk.Button(self.A_Menu_frame,text="Βάρδιες Μηχανικών",command= self.Mechanics_clock_in  ,font="bold",bg="gray",fg="black",width=20,height=1)
      self.button2.pack(side="top",pady=10) 
      self.button_exit=tk.Button(self.A_Menu_frame,text="Exit",command= root.destroy,font="bold",bg="red",fg="white",width=20,height=1)
      self.button_exit.pack(side="top",padx=5,pady=10)

   

   def Costumers_reviews(self):
      self.A_Menu_frame.pack_forget()
      As.Admin(self.root)

   def Mechanics_clock_in(self):
     self.A_Menu_frame.pack_forget()
     Am.admin_Mechanic(self.root)
      