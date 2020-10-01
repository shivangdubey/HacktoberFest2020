import tkinter
root=tkinter.Tk()
root.geometry("400x550")
root.title("Simple Calculator")
root.resizable(0,0)
###############
def show(numbers):
    global value
    value=value+str(numbers)
    name.set(value)


##############
def clear():
    global value
    value=""
    name.set("")


####################
def equal():
    global value
    data=str(eval(value))
    name.set(data)
    value=""
###############

def backspace():
    value=name.get()
    value1=value[:-1]
    name.set(value1
             )
    
###############

    
value=""    
name=tkinter.StringVar()
a=tkinter.Entry(root,text="",textvariable=name,bd=15,bg="lightgrey",font=("bold",25),justify="right")
a.place(x=0,y=10)
b=tkinter.Button(root,text="CL",font=("bold",20),command=clear,bg="lightblue",bd=5)
c=tkinter.Button(root,text="BS",font=("bold",20),command=backspace,bg="lightblue",bd=5)
d=tkinter.Button(root,text=" % ",font=("bold",20),command=lambda:show("%"),bg="lightblue",bd=5)
e=tkinter.Button(root,text=" / ",font=("bold",20),command=lambda:show("/"),bg="lightblue",bd=5)
f=tkinter.Button(root,text=" 7 ",font=("bold",20),command=lambda:show(7),bg="lightblue",bd=5)
g=tkinter.Button(root,text=" 8 ",font=("bold",20),command=lambda:show(8),bg="lightblue",bd=5)
h=tkinter.Button(root,text=" 9 ",font=("bold",20),command=lambda:show(9),bg="lightblue",bd=5)
i=tkinter.Button(root,text=" 4 ",font=("bold",20),command=lambda:show(4),bg="lightblue",bd=5)
j=tkinter.Button(root,text=" 5 ",font=("bold",20),command=lambda:show(5),bg="lightblue",bd=5)
k=tkinter.Button(root,text=" 6 ",font=("bold",20),command=lambda:show(6),bg="lightblue",bd=5)
l=tkinter.Button(root,text=" 1 ",font=("bold",20),command=lambda:show(1),bg="lightblue",bd=5)
m=tkinter.Button(root,text=" 2 ",font=("bold",20),command=lambda:show(2),bg="lightblue",bd=5)
n=tkinter.Button(root,text=" 3 ",font=("bold",20),command=lambda:show(3),bg="lightblue",bd=5)
o=tkinter.Button(root,text=" * ",font=("bold",20),command=lambda:show("*"),bg="lightblue",bd=5)
p=tkinter.Button(root,text=" - ",font=("bold",20),command=lambda:show("-"),bg="lightblue",bd=5)
q=tkinter.Button(root,text=" + ",font=("bold",20),command=lambda:show("+"),bg="lightblue",bd=5)
r=tkinter.Button(root,text="      =      ",font=("bold",20),command=equal,bg="lightblue",bd=5)
s=tkinter.Button(root,text=" 0 ",font=("bold",20),command=lambda:show(0),bg="lightblue",bd=5)
t=tkinter.Button(root,text=" . ",font=("bold",20),command=lambda:show("."),bg="lightblue",bd=5
                 )
b.place(x=10,y=90)
f.place(x=10,y=170)
i.place(x=10,y=270)
l.place(x=10,y=370)
t.place(x=10,y=470)
c.place(x=100,y=90)
g.place(x=100,y=170)
j.place(x=100,y=270)
m.place(x=100,y=370)
s.place(x=100,y=470)
d.place(x=200,y=90)
h.place(x=200,y=170)
k.place(x=200,y=270)
n.place(x=200,y=370)
t.place(x=10,y=470)
r.place(x=200,y=470)
e.place(x=300,y=90)
o.place(x=300,y=170)
p.place(x=300,y=270)
q.place(x=300,y=370)
root.mainloop()
