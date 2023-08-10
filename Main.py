print(" ")
from tkinter import *
import os
root=Tk()
l1=Label(root,font=("Consolas 16 bold"),text="What do you want to with Triumvirate tool")
l1.pack()
def helloCallBack(y):
   x=y
   if x==1:
      root.iconify()
      os.system('graphs.py')
   elif x==2:
      root.iconify()
      os.system('DataBase.py') 
   else:
      root.iconify()
      os.system('hangman.py')
e=Button(root, font=("Consolas 13 bold"),text ="Data visualisation tool", command=lambda : helloCallBack(1))
e.pack()
c=Button(root, font=("Consolas 13 bold"),text ="Ticket managment system and database", command=lambda : helloCallBack(2))
c.pack()
d=Button(root, font=("Consolas 13 bold"),text ="Play Hangman Game", command=lambda : helloCallBack(3))
d.pack()
root.mainloop()




