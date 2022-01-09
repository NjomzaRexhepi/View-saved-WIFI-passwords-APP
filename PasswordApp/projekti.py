from tkinter import *
import os
import subprocess
import re
import sys

from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()

window.resizable(0,0)
window.title("Int-Sec WiFi Passwords")
window.attributes('-fullscreen', False)
window.configure(background='#003366')
img = PhotoImage(file="4.png")
img = Image.open("4.png")
resized_image= img.resize((750,500), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized_image)
label = Label(
    window,
    image=img
)
label.place(x=0, y=0)
text = Label(window, text="Find All Saved Wifi Passwords", bg='black', fg = "powderblue" ,
		font = "Arial 14"
  )
text.place(relx=0.30,rely=0.05) 

window.geometry('750x500')

def help():  
    
    
    messagebox.showinfo('Help', 'Click the buttons to see the results!')
    
menubar = Menu(window)  
menubar.add_command(label="Help", command=help)  
menubar.add_command(label="Quit", command=window.quit) 
  
def openNewWindow(): 
      
 
    newWindow = Toplevel(window) 
  

    newWindow.title("New Window") 
  
  
    newWindow.geometry("700x600") 
  
  
    os.system("password.py")
   

    with open("final1.txt", "r") as f:
     Label(newWindow, text=f.read()).pack()

    window.mainloop()
 

def openNewWindow1(): 
      
    
    os.system("kompleksiteti.py")
    
   

    window.mainloop()
    
def openNewWindow2():
    
    os.system("pg2.py")
    
    window.mainloop()
    
def openNewWindow3():
    os.system("aboutus.py")
    window.mainloop() 
       

btn = Button(window,text='Show Wi-Fi pass',  bg='black', fg='powderblue', command=openNewWindow)
btn2 = Button(window,text='Show Complexity',  bg='black', fg='powderblue',command=openNewWindow1)
btn3 = Button(window,text='Password generator',  bg='black', fg='powderblue', command=openNewWindow2)
btn4=Button(window, text='About our app', bg='black', fg='powderblue', command=openNewWindow3)

btn.grid(column=0,row=0)
btn.place(relx=0.1, rely=0.5)
btn2.grid(column=0,row=0)
btn2.place(relx=0.4, rely=0.5)
btn3.grid(column=0,row=0)
btn3.place(relx=0.7, rely=0.5)
btn4.grid(column=1, row=1)
btn4.place(relx=0.1, rely=0.9)

window.config(menu=menubar)  
window.mainloop()
window.mainloop()