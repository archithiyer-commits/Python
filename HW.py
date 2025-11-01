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
                  text="Hey User! Welcome to Password strength check application.",
                  bg='light blue')
label1.place(relx=0.5, y=340, anchor=tk.CENTER)
def msg():
    MsgBox = messagebox.showinfo("Alert", "Do you want to check your password strength?")
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
    top.title("Password strength checker")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")
    label = tk.Label(top, text="Enter Password", bg='light grey')
    entry = tk.Entry(top)
   
    lbl = tk.Label(top, text="Here is a rating for your password strength. ", bg='light grey')
   
    l1 = tk.Label(top, text="Password Strength", bg='light grey')
    t1 = tk.Entry(top)

    def strength():
        try:
            length_pw=len(entry.get())            
            t1.delete(0, tk.END)
            stngth = "Weak"
            if(length_pw >5):
                stngth = "Medium"
            if(length_pw>8):
                stngth = "Strong"
            if(length_pw>12):
                stngth = "Very Strong"

            t1.insert(tk.END, str(stngth))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = tk.Button(top, text='Calculate', command=strength, bg='brown', fg='white')

    # Centering Widgets in the Top Window
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)
    l1.place(x=180, y=200)
    t1.place(x=270, y=200)

# Run main window
root.mainloop()