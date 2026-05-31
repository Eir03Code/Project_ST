import tkinter as tk
import questions_screen as Qs
import User_services as Us
import Rate_experience_screen as Res
import Confirmation_screen as Cs


class Description_question:

   def __init__ (self,root,answers,rating):
      self.root=root
      self.answers=answers
      self.rating=rating
      self.description_frame=tk.Frame(self.root,bg="black")
      self.description_frame.pack(pady=50)
      self.description_label=tk.Label(self.description_frame,text="Θα Θέλατε να Αφήσετε Περιγραφή της Εμπειρίας σας;",fg="white",bg="black",font=("bold",15))
      self.description_label.pack(side="top",pady=10) 
      self.description_label_2=tk.Label(self.description_frame,text="Περιγραφή",fg="white",bg="black",font=("bold",20))
      self.button_for_description=tk.Button(self.description_frame,text="Βεβαίως",command= self.set_description,font="bold",bg="gray",fg="white",width=20,height=1)
      self.button_for_description.pack(side="top",padx=8,pady=10)
      self.button_for_disagree=tk.Button(self.description_frame,text="Όχι Τώρα",command= self.lets_continue,font="bold",bg="red",fg="white",width=20,height=1)
      self.button_for_disagree.pack(side="top",padx=8,pady=5)
      self.Entry3=tk.Text(self.description_frame,width=50,height=7)
      self.button_continue=tk.Button(self.description_frame,text="Συνέχεια",command= self.lets_continue,font="bold",bg="green",fg="white",width=15,height=1)

   def set_description(self):
      self.description_label.pack_forget()
      self.button_for_description.pack_forget()
      self.button_for_disagree.pack_forget()
      self.description_label_2.pack(side="top")
      self.Entry3.pack(side="top",pady=20)  
      self.button_continue.pack(side="top",padx=10,pady=10)


   def lets_continue(self):
      self.description_text=self.Entry3.get("1.0","end-1c")
      Us.Submit_answers(self.answers,self.rating,self.description_text)
      self.description_frame.pack_forget()
      Cs.Confirmation(self.root)