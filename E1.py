import tkinter as tk

window = tk.Tk()
window.title("Event handler")
window.gemetry("100x100")

def handle_keypress(event):
    """Print the charecter associated to key presssed"""
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nThe button was clicked!")

button = tk.Button(text="Click me!") 
button.pack()

button.bind("Button-1", handle_click)

window.mainloop()