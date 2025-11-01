import tkinter as tk

root = tk.Tk()
root.title('Age Calculator App')
root.geometry('400x400')

frame = tk.Frame(master=root, height=400, width=400, bg="#d0efff")

lbl1 = tk.Label(frame, text="Full Name", bg="#3895D3", fg='white', width=12)
lbl2 = tk.Label(frame, text="Date of birth", bg="#3895D3", fg='white', width=12)
lbl3 = tk.Label(frame, text="Month of birth", bg="#3895D3", fg='white', width=12)
lbl4 = tk.Label(frame, text="Year of birth", bg="#3895D3", fg='white', width=12)

name_entry = tk.Entry(frame)
date_entry = tk.Entry(frame)
month_entry = tk.Entry(frame)
year_entry = tk.Entry(frame)

def display():
    name = name_entry.get()
    age_yrs = 2025 - int(year_entry.get())
    if(int(month_entry.get()) > 11):
        age_yrs = age_yrs - 1
    age = str(age_yrs)
    greet = "\nHey " + name
    message = "\nYou are " + age + " years  old !"
    textbox.insert(tk.END, greet)
    textbox.insert(tk.END, message)

textbox = tk.Text(bg="#BEBEBE", fg="black")

btn = tk.Button(text="Calculate Age", command=display, bg="red")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
date_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
month_entry.place(x=150, y=140)
btn.place(x=130, y=250)
textbox.place(y=250)
lbl4.place(x=20, y=200)
year_entry.place(x=150, y=200)
root.mainloop()
