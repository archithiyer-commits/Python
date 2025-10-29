import tkinter as tk
from tkinter import messagebox

# Setting up Main Window
root = tk.Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

label = tk.Label(root, bg='light blue')
label.place(x=180, y=20)

label1 = tk.Label(root,
                  text="Hey User! Welcome to Denomination Counter Application.",
                  bg='light blue')
label1.place(relx=0.5, y=340, anchor=tk.CENTER)

# Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

# Adding Buttons to the main window
button1 = tk.Button(root,
                    text="Let's get started!",
                    command=msg,
                    bg='brown',
                    fg='white')
button1.place(x=260, y=360)

# Function for opening new/top window
def topwin():
    top = tk.Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")

    label = tk.Label(top, text="Enter total amount", bg='light grey')
    entry = tk.Entry(top)
    lbl = tk.Label(top, text="Here are number of notes for each denomination", bg='light grey')

    l1 = tk.Label(top, text="2000", bg='light grey')
    l2 = tk.Label(top, text="500", bg='light grey')
    l3 = tk.Label(top, text="100", bg='light grey')

    t1 = tk.Entry(top)
    t2 = tk.Entry(top)
    t3 = tk.Entry(top)

    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, tk.END)
            t2.delete(0, tk.END)
            t3.delete(0, tk.END)

            t1.insert(tk.END, str(note2000))
            t2.insert(tk.END, str(note500))
            t3.insert(tk.END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = tk.Button(top, text='Calculate', command=calculator, bg='brown', fg='white')

    # Centering Widgets in the Top Window
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

# Run main window
root.mainloop()
