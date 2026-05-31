import tkinter as tk
import questions_screen as Qs
import User_services as Us
import Description_q_screen as Ds
class Rate_experience:

   def __init__ (self,root,answers):
      self.root=root
      self.answers=answers
      self.stars=[]
      self.Rate_experience_frame=tk.Frame(self.root,bg="black")
      self.Rate_experience_frame.pack(pady=50)
      self.Rate_experience_label=tk.Label(self.Rate_experience_frame,text="Βαθμολογείστε παρακάτω την Εμπειρία σας στο Garage μας",fg="white",bg="black",font=("bold",15)).pack(side="top",padx=10,pady=50)
      self.create_star_system()


   def set_rate(self,value):
      for i in range(5):
         if i<value:
            self.stars[i].config(text="★")
         else:
            self.stars[i].config(text="☆")
      
      self.rating=value
      self.Rate_experience_frame.pack_forget()
      Ds.Description_question(self.root,self.answers,self.rating)
      

   def create_star_system(self):
       for i in range(5):
        self.star=tk.Button(self.Rate_experience_frame,text="☆",bg="gray",font=("Arial",25),bd=0,command=lambda v=i+1:self.set_rate(v))


        self.star.pack(side="left",padx=10)
   
        self.stars.append(self.star)