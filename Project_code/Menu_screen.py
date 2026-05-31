
import tkinter as tk
from Review_screen import Start_review


class Menu:

   def __init__ (self,root):
      
      self.root=root
      self.Menu_frame=tk.Frame(self.root,bg="black")
      self.Menu_frame.pack(pady=50)
      self.Menu_label=tk.Label(self.Menu_frame,text="Menu",fg="white",bg="black",font=("bold",20))
      self.Menu_label.pack(side="top",padx=10,pady=10)
      self.button2=tk.Button(self.Menu_frame,text="Αξιολόγηση Υπηρεσίας",command= self.activate_review  ,font="bold",bg="gray",fg="black",width=20,height=1)
      self.button2.pack(side="top",pady=10) 
      self.button_exit=tk.Button(self.Menu_frame,text="Exit",command= root.destroy,font="bold",bg="red",fg="white",width=20,height=1)
      self.button_exit.pack(side="top",padx=5,pady=10)
      self.check_if_has_given_answer()
   

   def activate_review(self):
      self.Menu_frame.pack_forget()
      Start_review(self.root)

   def check_if_has_given_answer(self):
     import User_services as Us
     res= Us.check_if_answers()
     if res==1:
         self.button2.config(state="disabled")
      