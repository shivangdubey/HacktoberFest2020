from tkinter import *
import tkinter.messagebox as tmsg
import math
from math import log, e, sin, cos, tan
from math import cosh as sec
from math import sinh as cosec
from math import tanh as cot

root = Tk()
root.geometry("320x650")
root.title("Calculator")
root.config(bg="skyblue")


def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(entry_widget.get())
            except Exception as e:
                print(e)
                value = "Error"
                tmsg.showinfo("Invalid Input", "Please Enter Valid Inputs")

        scvalue.set(value)
        entry_widget.icursor(END)
        entry_widget.update()

    elif text == "C":
        scvalue.set("")
        entry_widget.update()

    elif text == "←":
        val = scvalue.get()
        scvalue.set(val[:-1])

    elif text =="1/x":
        try:
            value = 1/float(scvalue.get())
        except Exception as e:
            print(e)
            value = "Error"
            tmsg.showinfo("Invalid Input", "Please Enter Valid Inputs")
        scvalue.set(value)
        entry_widget.icursor(END)
        entry_widget.update()

    elif text =="|x|":
        scvalue.set(abs(float(scvalue.get())))

    elif text =="n!":
        try:
            value = math.factorial(int(scvalue.get()))
        except Exception as e:
            print(e)
            value = "Error"
            tmsg.showinfo("Invalid Input", "Please Enter Valid Inputs")
        scvalue.set(value)
        entry_widget.icursor(END)
        entry_widget.update()
    elif text=="x^2":
        scvalue.set(pow(float(scvalue.get()),2))

    elif text in extra_buttons:
        if text != "e":
            scvalue.set(scvalue.get() + f"{text}()")

        else:
            scvalue.set(scvalue.get() + f"{text}**")

    else:
        scvalue.set(scvalue.get() + str(text))
        entry_widget.update()

    print(text)


scvalue = StringVar()
scvalue.set("")
entry_widget = Entry(root, textvar=scvalue, font="lucida 20 bold", borderwidth=4, relief=SUNKEN)
entry_widget.pack(pady=15, fill=X, padx=5, ipadx=10, ipady=3)

list1 = 9
outer_frame = Frame(root, bg="blue", relief=SUNKEN, borderwidth=6)

symbols = ["+", "-", "*"]
for i in range(3):
    f = Frame(outer_frame, bg="grey")

    b = Button(f, text=list1, font="lucida 16 ", height=2, width=4)
    b.pack(padx=5, pady=5, side=LEFT)
    b.bind("<Button-1>", click)

    b1 = Button(f, text=list1 - 1, font="lucida 16", height=2, width=4)
    b1.pack(padx=5, pady=5, side=LEFT)
    b1.bind('<Button-1>', click)

    b2 = Button(f, text=list1 - 2, font="lucida 16", height=2, width=4)
    b2.pack(padx=5, pady=5, side=LEFT)
    b2.bind('<Button-1>', click)

    b3 = Button(f, text=symbols[i], font="lucida 16", height=2, width=4)
    b3.pack(padx=5, pady=5, side=LEFT)
    b3.bind('<Button-1>', click)

    list1 -= 3
    f.pack()


def row(a, item, c, d):
    f1 = Frame(outer_frame, bg="grey")
    b = Button(f1, text=a, font="lucida 16", height=2, width=4)
    b.pack(padx=5, pady=5, side=LEFT)
    b.bind("<Button-1>", click)

    b = Button(f1, text=item, font="lucida 16", height=2, width=4)
    b.pack(padx=5, pady=5, side=LEFT)
    b.bind("<Button-1>", click)

    b = Button(f1, text=c, font="lucida 16", height=2, width=4)
    b.pack(padx=5, pady=5, side=LEFT)
    b.bind("<Button-1>", click)

    b = Button(f1, text=d, font="lucida 16", height=2, width=4)
    b.pack(padx=5, pady=5, side=LEFT)
    b.bind("<Button-1>", click)
    f1.pack()


outer_frame.pack(padx=10, pady=10)

list1 = ["C", "0", ".", "/", "00", "←", "=", "%","1/x","|x|","n!","x^2"]
row(list1[0], list1[1], list1[2], list1[3])
row(list1[4], list1[5], list1[6], list1[7])
row(list1[8], list1[9], list1[10], list1[11])

extra_buttons = ["log", "e", "sin", "cos", "tan", "cosec", "sec", "cot"]


def plot_more():
    more.set("Less")
    frame = Frame(root, bg="green", padx=5, pady=5, relief=SUNKEN, borderwidth=6)
    f = Frame(frame, bg="grey", )
    for j in range(4):
        b = Button(f, text=extra_buttons[j], font="lucida 16", height=2, width=4)
        b.pack(side=LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)
    f.pack()

    f = Frame(frame, bg="grey", )
    for j in range(4):
        b = Button(f, text=extra_buttons[j + 4], font="lucida 16", height=2, width=4)
        b.pack(side=LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)
    f.pack()
    frame.pack(padx=5)


more = StringVar()
more.set("More")

plot_more()

root.mainloop()
