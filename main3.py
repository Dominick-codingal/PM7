from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Box Demo")
root.geometry("300x250")

def msg():
    messagebox.showwarning("Alert!", "Stop! Virus found")
    
def show_warning():
    messagebox.showwarning("Warning", "Suspicious file detected!") 
def show_error():
    messagebox.showerror("Error", "System crash detected!")
    
def ask_question():
    response = messagebox.askyesno("Confirm", "Do you want to delete the file?")
    
    if response == True:
        print("User chose YES")
    else:
        print("User chose No")    
    
button_warning = Button(root, text = "show warning", command=show_warning, bg="red") 
button_error= Button(root, text = "show error", command=show_error,  bg="yellow") 
button_question = Button(root, text = "show warning", command=ask_question)     
button_scan = Button(root, text = "Scan For Virus", command=msg)    

button_warning.place(x=40, y=30)
button_error.place(x=150, y=30)
button_question.place(x=40, y=80)
button_scan.place(x=150, y=80)

root.mainloop()