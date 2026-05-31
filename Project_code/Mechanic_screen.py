import tkinter as tk
import User_services as Us


class Mechanic:

   def __init__ (self,root):
      
      self.root=root
      self.Menu_frame=tk.Frame(self.root,bg="black")
      self.Menu_frame.pack(pady=50)
      self.Menu_label=tk.Label(self.Menu_frame,text="Mechanic Menu",fg="white",bg="black",font=("bold",20))
      self.Menu_label.pack(side="top",padx=10,pady=10)
      self.button_c5=tk.Button(self.Menu_frame,text="Έναρξη Βάρδιας",command= self.clock_in  ,font="bold",bg="gray",fg="black",width=20,height=1)
      self.button_c5.pack(side="top",padx=5,pady=10) 
      self.button_exit=tk.Button(self.Menu_frame,text="Exit",command= root.destroy,font="bold",bg="red",fg="white",width=20,height=1)
      self.button_exit.pack(side="top",padx=5,pady=10)
   
      
   def clock_in(self):
     import User_services as Us
     Us.set_clock_in()
     self.button_c5.config(state="disabled")