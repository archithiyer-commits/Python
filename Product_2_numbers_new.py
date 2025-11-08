import tkinter as tk
from tkinter import messagebox

# Setting up Main Window
root = tk.Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('400x400')

label = tk.Label(root, bg='light blue')
label.place(x=180, y=20)
label1 = tk.Label(root,
                  text="Hey User! Welcome to Multiplication application.",
                  bg='light blue')
label1.place(relx=0.5, y=340, anchor=tk.CENTER)
def msg():
    MsgBox = messagebox.showinfo("Alert", "Do you want to Multiply 2 numebers?")
    if MsgBox == 'ok':
        topwin()
button1 = tk.Button(root,
                    text="Let's get started!",
                    command=msg,
                    bg='brown',
                    fg='white')
button1.place(x=260, y=360)

# Function for opening new/top window

def topwin():
    top = tk.Toplevel()
    top.title("Product of 2 Numbers")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")
    

    label1 = tk.Label(top, text="Enter Number 1", bg='light grey')
    label2 = tk.Label(top, text="Enter Number 2", bg='light grey')
    label3 = tk.Label(top, text="Answer", bg='light grey')
    
    entry1 = tk.Entry(top)    
    entry2 = tk.Entry(top)
    result1 = tk.Entry(top)
       

    def strength():
        try:
            stngth = int(entry2.get())*int(entry1.get())
            result1.insert(tk.END, str(stngth))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = tk.Button(top, text='Calculate', command=strength, bg='brown', fg='white')

    # Centering Widgets in the Top Window
    label1.place(x=10, y=50)
    entry1.place(x=120, y=50)

    label2.place(x=10, y=100)
    entry2.place(x=120,y=100)
    
    label3.place(x=10, y=150)
    result1.place(x=120,y=150)
    
    btn.place(x=240, y=200)
    

# Run main window
root.mainloop()