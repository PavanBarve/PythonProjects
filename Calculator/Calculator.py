import tkinter as tk
from tkinter import RIDGE, Entry, Button

root = tk.Tk()

root.title("Calculator")
root.geometry("340x340")
root.iconbitmap("calculator_icon.ico")

# Entry widget to show calculations
inp = Entry(root, width=32, borderwidth=6, relief=RIDGE)
inp.grid(pady=20, row=0, sticky='w', padx=30)


class GridButtons:
    def __init__(self):
        pass

    def nine(self):
        inp.insert("end", "9")

    def eight(self):
        inp.insert("end", "8")

    def seven(self):
        inp.insert("end", "7")

    def six(self):
        inp.insert("end", "6")

    def five(self):
        inp.insert("end", "5")

    def four(self):
        inp.insert("end", "4")

    def three(self):
        inp.insert("end", "3")

    def two(self):
        inp.insert("end", "2")

    def one(self):
        inp.insert("end", "1")

    def zero(self):
        inp.insert("end", "0")

    def double_zero(self):
        inp.insert("end", "00")

    def dot(self):
        inp.insert("end", ".")

    def plus(self):
        inp.insert("end", "+")

    def minus(self):
        inp.insert("end", "-")

    def mul(self):
        inp.insert("end", "*")

    def devide(self):
        inp.insert("end", "/")

    def modulus(self):
        inp.insert("end", "%")

    def result(self):
        if inp.get() == "":
            inp.insert("end", "error")
        elif inp.get()[0] == "0":
            inp.delete(0, "end")
            inp.insert("end", "error")
        else:
            res = inp.get()
            res = eval(res)
            inp.insert("end", "=")
            inp.insert("end", res)

    def clear(self):
        inp.delete(0, "end")


gb = GridButtons()

clear_btn = Button(root, text="C", width=4,borderwidth=3, command=gb.clear, bg="red", fg="white", relief=RIDGE)
clear_btn.grid(row=0, sticky="w", padx=250)

nine = Button(root, text="9", width=4, command=gb.nine, borderwidth=3, bg="blue", fg="white", relief=RIDGE)
nine.grid(row=1, sticky="w", padx=30,pady=10)
eight = Button(root, text="8", width=4, command=gb.eight, borderwidth=3, bg="blue", fg="white", relief=RIDGE)
eight.grid(row=1, sticky="w", padx=90,pady=10)
seven = Button(root, text="7", width=4, command=gb.seven, borderwidth=3, bg="blue", fg="white", relief=RIDGE)
seven.grid(row=1, sticky="w", padx=150,pady=10)
plus = Button(root, text="+", width=4, command=gb.plus, borderwidth=3, bg="blue", fg="white", relief=RIDGE)
plus.grid(row=1, sticky="w", padx=250,pady=10)

six = Button(root, text="6", width=4, command=gb.six, borderwidth=3, bg="blue", fg="white", relief=RIDGE)
six.grid(row=2, sticky="w", padx=30, pady=10)
five = Button(root, text="5", width=4, command=gb.five, borderwidth=3, bg="blue", fg="white", relief=RIDGE)
five.grid(row=2, sticky="w", padx=90, pady=10)
four = Button(root, text="4", width=4, command=gb.four, borderwidth=3, bg="blue", fg="white", relief=RIDGE)
four.grid(row=2, sticky="w", padx=150, pady=10)
minus = Button(root, text="-", width=4, command=gb.minus, borderwidth=3, bg="blue", fg="white", relief=RIDGE)
minus.grid(row=2, sticky="w", padx=250, pady=10)

three = Button(root, text="3", width=4, command=gb.three, borderwidth=3, bg="blue", fg="white", relief=RIDGE)
three.grid(row=3, sticky="w", padx=30, pady=10)
two = Button(root, text="2", width=4, command=gb.two, borderwidth=3, bg="blue", fg="white", relief=RIDGE)
two.grid(row=3, sticky="w", padx=90, pady=10)
one = Button(root, text="1", width=4, command=gb.one, borderwidth=3, bg="blue", fg="white", relief=RIDGE)
one.grid(row=3, sticky="w", padx=150, pady=10)
mul = Button(root, text="*", width=4, command=gb.mul, borderwidth=3, bg="blue", fg="white", relief=RIDGE)
mul.grid(row=3, sticky="w", padx=250, pady=10)

zero = Button(root, text="0", width=4, command=gb.zero, borderwidth=3, bg="blue", fg="white", relief=RIDGE)
zero.grid(row=4, sticky="w", padx=30, pady=10)
double_zero = Button(root, text="00", width=4, command=gb.double_zero, borderwidth=3, bg="blue", fg="white",
                     relief=RIDGE)
double_zero.grid(row=4, sticky="w", padx=90, pady=10)
dot = Button(root, text=".", width=4, command=gb.dot, borderwidth=3, bg="blue", fg="white", relief=RIDGE)
dot.grid(row=4, sticky="w", padx=150, pady=10)
divide = Button(root, text="/", width=4, command=gb.devide, borderwidth=3, bg="blue", fg="white", relief=RIDGE)
divide.grid(row=4, sticky="w", padx=250, pady=10)

result = Button(root, text="=", width=21, command=gb.result,borderwidth=3, bg="red", fg="white", relief=RIDGE)
result.grid(row=5, sticky="w", padx=30, pady=10)
mod = Button(root, text="%", width=4, command=gb.modulus,borderwidth=3, bg="blue", fg="white", relief=RIDGE)
mod.grid(row=5, sticky="w", padx=250, pady=10)

root.mainloop()
