from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("300x200")

def Handle_Keypress(event):
    """Print the character associated to the keypressed"""
    print(event.char)
    
window.bind("<Key>", Handle_Keypress)    
    
def handle_click(event):
    print("\nThe button was clicked!")

button = Button(text="Click me!")
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()
