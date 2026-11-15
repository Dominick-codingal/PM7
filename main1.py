from tkinter import *
from datetime import date

root = Tk()
root.title("Getting started with Widgets")
root.geometry('600x500')
lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=30)

name_lbl = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()
    
    text_box.delete('1.0', END)
    
    greet = "Hello " + name + "\n"
    message = "Welcome to my app! \nToday's date is: "
    
    text_box.insert(END, greet)
    
    text_box.insert(END, message)
    
    text_box.insert(END, date.today())
    
text_box = Text(height=7)    
btn = Button(text="Begin", command=display, bg="#1261A0", fg='white')

lbl.pack(pady=10)
name_lbl.pack()
name_entry.pack(pady=5)
btn.pack(pady=10)
text_box.pack() 

root.mainloop()   