from tkinter import *
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
