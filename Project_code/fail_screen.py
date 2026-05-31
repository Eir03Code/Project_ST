import tkinter as tk
import Menu_screen as Mc
import time 


class fail:

    def __init__ (self,root):
      
      self.root=root
      self.fail_frame=tk.Frame(self.root,bg="black")
      self.fail_frame.pack(pady=10)
      self.fail_label=tk.Label(self.fail_frame,text="Λυπάμαι Αποτυχία Ολοκλήρωσης της Διαδικασίας",fg="red",bg="black",font=("bold",20)).pack(side="top",padx=10,pady=10)
   
      self.fail_frame.after(2000,self.go_menu)

    def go_menu(self):
         
      self.fail_frame.pack_forget()
      Mc.Menu(self.root)