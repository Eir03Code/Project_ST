import tkinter as tk
import User_services as Us
import Rate_experience_screen as Rt

class Questionaire:

    def __init__ (self,root):
      self.i=0
      self.answers=[]
      self.root=root
      self.Questionaire_frame=tk.Frame(self.root,bg="black")
      self.Questionaire_frame.pack(pady=40)
      self.Questionaire_label=tk.Label(self.Questionaire_frame,text="",fg="white",bg="black",font=("bold",14))
      self.Questionaire_label.pack(side="top",padx=10,pady=25)
      
      self.choice1=tk.Button(self.Questionaire_frame ,font="bold" ,bg="gray",fg="black",width=20,height=1)
      self.choice1.pack(side="top",pady=5) 

      self.choice2=tk.Button(self.Questionaire_frame ,font="bold",bg="gray",fg="black",width=20,height=1)
      self.choice2.pack(side="top",pady=5) 

      self.choice3=tk.Button(self.Questionaire_frame  ,font="bold",bg="gray",fg="black",width=20,height=1)
      self.choice3.pack(side="top",pady=5) 

      self.choice4=tk.Button(self.Questionaire_frame ,font="bold",bg="gray",fg="black",width=20,height=1)
      self.choice4.pack(side="top",pady=5) 
      self.show_questions()
            


    def show_questions(self):
      
      self.questions=Us.load_questions()
      
      self.the_question=self.questions["questions"][self.i]

      self.Questionaire_label.config(text=self.the_question['question'])

      self.choices=self.the_question['choices']


      self.choice1.config(text=self.choices[0],command=lambda: self.procedure(self.choices[0]))
      self.choice2.config(text=self.choices[1],command=lambda: self.procedure(self.choices[1]))
      self.choice3.config(text=self.choices[2],command=lambda: self.procedure(self.choices[2]))
      self.choice4.config(text=self.choices[3],command=lambda: self.procedure(self.choices[3]))
      
    
    def procedure(self,selected_answer):
        self.answers.append(selected_answer) 
        self.i += 1
        if self.i < len(self.questions["questions"]):
          self.show_questions()
        elif self.i == len(self.questions["questions"]):
          self.Questionaire_frame.pack_forget()
          Rt.Rate_experience(self.root,self.answers)
          

