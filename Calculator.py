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
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("250x520")
root.title("Calculator")
root.config(bg="SkyBlue1")


def click(event):
    global scvalue
    text=event.widget.cget("text")


    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(entry_widget.get())
            except Exception as e:
                print(e)
                value="Error"
                tmsg.showinfo("Invalid Input","Please Enter Valid Inputs")

        scvalue.set(value)
        entry_widget.update()
    elif text== "C":
        scvalue.set("")
        entry_widget.update()
    else:
        scvalue.set(scvalue.get()+str(text))
        entry_widget.update()

    print(text)

scvalue = StringVar()
scvalue.set("")
entry_widget = Entry(root,textvar=scvalue,font="lucida 20 bold",borderwidth=4,relief=SUNKEN)
entry_widget.pack(pady=15,fill=X,padx=5,ipadx=10,ipady=3)

list1=9
outer_frame=Frame(root,bg="blue",relief=SUNKEN,borderwidth=6)
for i in range(3):
    f= Frame(outer_frame,bg="grey")
    b=Button(f,text=list1,font="lucida 16 ",padx=10,pady=10)
    b.pack(padx=5,pady=5,side=LEFT)
    b.bind("<Button-1>" ,click)

    b1 = Button(f,text=list1-1,font="lucida 16",padx=10,pady=10)
    b1.pack(padx=5,pady=5,side=LEFT)
    b1.bind('<Button-1>',click)

    b2= Button(f,text=list1-2,font="lucida 16",padx=10,pady=10)
    b2.pack(padx=5,pady=5,side=LEFT)
    b2.bind('<Button-1>',click)

    list1=list1-3
    f.pack()

def row(a,item,c):
    f1 = Frame(outer_frame,bg="grey")
    b = Button(f1, text=a, font="lucida 16", padx=10, pady=10)
    b.pack(padx=5, pady=5, side=LEFT)
    b.bind("<Button-1>",click)
    b = Button(f1, text=item, font="lucida 16", padx=10, pady=10)
    b.pack(padx=5, pady=5, side=LEFT)
    b.bind("<Button-1>",click)
    b = Button(f1, text=c, font="lucida 15", padx=10, pady=10)
    b.pack(padx=5, pady=5, side=LEFT)
    b.bind("<Button-1>",click)
    f1.pack()

outer_frame.pack(padx=10,pady=10)

list1=["0","=","C","+","/","%","00","*","."]
row(list1[0],list1[1],list1[2])
row(list1[3],list1[4],list1[5])
row(list1[6],list1[7],list1[8])
root.mainloop()
