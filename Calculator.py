from tkinter import *
root = Tk()
def click(event):
    global scrValue
    text = event.widget.cget("text")
    if text == "=":
        if scrValue.get().isdigit():
            value = int(scrValue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                value = "ERROR"
        scrValue.set(value)
        screen.update()
    elif text == "C":
        scrValue.set("")
        screen.update()
    
    else:
        scrValue.set(scrValue.get()+text)
        screen.update()

root.geometry("744x1200")
root.title("Calculator")
root.wm_iconbitmap("icon.png")
scrValue = StringVar()
scrValue.set("")
screen=Entry(root,textvariable=scrValue,font="Helvatica 18 bold",bg="grey",fg="white")
screen.pack(fill=X,ipadx=18,pady=13,padx=15)
listButton = ["9","8","7"]
f = Frame(root,bg="light green")
for i in listButton:
    b=Button(f,text=f"{i}",padx=28, pady=18, font="lucida 25 bold",bg="grey")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>",click)
f.pack()

f1 = Frame(root,bg="light green")
listButton1 = ["6","5","4"]
for i in listButton1:
    b=Button(f1,text=f"{i}",padx=28, pady=18, font="lucida 25 bold",bg="grey")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>",click)

f1.pack()

f2 = Frame(root,bg = "light green")
listButton2 = ["3","2","1"]
for i in listButton2:
    b=Button(f2,text=f"{i}",padx=28, pady=18, font="lucida 25 bold",bg="grey")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>",click)
f2.pack()


f3 = Frame(root,bg = "light green")
listButton2 = ["0","+","-"]
for i in listButton2:
    b=Button(f3,text=f"{i}",padx=29, pady=18, font="lucida 25 bold",bg="grey")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>",click)
f3.pack()

f4 = Frame(root,bg = "light green")
listButton2 = ["*","/","%"]
for i in listButton2:
    b=Button(f4,text=f"{i}",padx=29, pady=18, font="lucida 25 bold",bg="grey")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>",click)
f4.pack()

f5 = Frame(root,bg="light green")
listButton3 = ["=","C","."]
for i in listButton3:
    b=Button(f5,text=f"{i}",padx=28, pady=18, font="lucida 25 bold",bg="grey")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>",click)
f5.pack()

root.configure(background="light blue")
root.mainloop()
