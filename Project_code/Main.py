import tkinter as tk
from Login_screen import Login
import User_services as Us

Us.create_users()
root=tk.Tk()
Login(root)
root.mainloop()

