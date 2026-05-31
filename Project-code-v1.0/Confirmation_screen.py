import tkinter as tk
import Menu_screen as Mc
import time 


class Confirmation:

    def __init__ (self,root):
      
      self.root=root
      self.false_ok_frame=tk.Frame(self.root,bg="black")
      self.false_ok_frame.pack(pady=10)
      self.saving=tk.Label(self.false_ok_frame,text="Aποθήκευση....",fg="green",bg="black",font=("bold",25))
      self.saving.pack(side="top",padx=10,pady=10)
      self.Success=tk.Label(self.false_ok_frame,text="Η Αξιολόγηση Ολοκληρθηκε με Επιτυχία",fg="green",bg="black",font=("bold",25))
      self.false_ok_frame.after(2000,self.ending_procedure)

    def ending_procedure(self):
      self.saving.pack_forget() 
      self.Success.pack(side="top",padx=10,pady=10)
      self.false_ok_frame.after(2000,self.go_menu)

    def go_menu(self):
      self.false_ok_frame.pack_forget()
      Mc.Menu(self.root)