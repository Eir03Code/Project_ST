import tkinter as tk
import fail_screen as f


class Start_review:

   def __init__ (self,root):
      
      self.root=root
      self.Review_frame=tk.Frame(self.root,bg="black")
      self.Review_frame.pack(pady=50)
      self.Review_label=tk.Label(self.Review_frame,text="Έχετε Παραλάβει το Οχημά Σας;",fg="white",bg="black",font=("bold",30)).pack(side="top",padx=10,pady=10)
   
      self.button3=tk.Button(self.Review_frame,text="Επιβεβαιώνω",command= self.start_questonaire  ,font="bold",bg="gray",fg="black",width=20,height=1)
      self.button3.pack(side="top",pady=20) 

      self.button4=tk.Button(self.Review_frame,text="Διαψεύδω",command= self.Fail_screen ,font="bold",bg="gray",fg="black",width=20,height=1)
      self.button4.pack(side="top") 

      self.button_exit=tk.Button(self.Review_frame,text="Exit",command= root.destroy,font="bold",bg="red",fg="white",width=20,height=1)
      self.button_exit.pack(side="top",pady=20)


   
   def start_questonaire(self):
      import questions_screen as Qs
      self.Review_frame.pack_forget()
      Qs.Questionaire(self.root)

   def Fail_screen(self):
      self.Review_frame.pack_forget()
      f.fail(self.root)