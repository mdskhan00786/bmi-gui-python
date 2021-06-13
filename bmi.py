import tkinter as tk

fg = '#2b2b2b'
bg = '#f1c159'

root = tk.Tk()
root.geometry('500x200')
root.title("Bmi App ")
root.configure(bg=bg)
bmi_var = tk.IntVar()

label_kg = tk.Label(root,text="Enter your Weight(kg): ",fg=fg,font=('Arial',15)).place(x=30, y=18)
label_h = tk.Label(root,text="Enter your height(m): ",fg=fg,font=('Arial',15)).place(x=30, y=54)
label_bmi = tk.Label(root,text="Your BMI is: ",fg=fg,font=('Arial',15)).place(x=30, y=90)
label_op = tk.Label(root,textvariable=bmi_var,fg=fg,font=('Arial',15)).place(x=250, y=90)

entry_kg = tk.Entry(root, font=('Arial',15))
entry_h = tk.Entry(root, font=('Arial',15))
entry_kg.place(x=250,y=18)
entry_h.place(x=250,y=54)

def calc():
    kg = float(entry_kg.get())
    height = float(entry_h.get())
    bmi = round(kg/(height**2),2)
    bmi_var.set(bmi)

button = tk.Button(root,text="Calculate", font=('Arial',15),fg=fg,command=calc).place(x=215, y=145)
root.mainloop()