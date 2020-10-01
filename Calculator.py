import tkinter
root=tkinter.Tk()
root.geometry("500x550")
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
name.set('0')
a=tkinter.Entry(root,text="",textvariable=name,bd=5,bg="black",font=("bold",25),justify="right",fg='white')
a.place(x=30,y=10)
b=tkinter.Button(root,text="AC",font=("bold",20),command=clear,bg="red",bd=5,width=2)
c=tkinter.Button(root,text="C",font=("bold",20),command=backspace,bg="darkblue",bd=5,width=2)
d=tkinter.Button(root,text=" % ",font=("bold",20),command=lambda:show("%"),bg="orange",bd=5,width=2)
e=tkinter.Button(root,text=" / ",font=("bold",20),command=lambda:show("/"),bg="orange",bd=5,width=2)
f=tkinter.Button(root,text=" 7 ",font=("bold",20),command=lambda:show(7),bg="grey",bd=5,width=2)
g=tkinter.Button(root,text=" 8 ",font=("bold",20),command=lambda:show(8),bg="grey",bd=5,width=2)
h=tkinter.Button(root,text=" 9 ",font=("bold",20),command=lambda:show(9),bg="grey",bd=5,width=2)
h=tkinter.Button(root,text=" 9 ",font=("bold",20),command=lambda:show(9),bg="grey",bd=5,width=2)
i=tkinter.Button(root,text=" 4 ",font=("bold",20),command=lambda:show(4),bg="grey",bd=5,width=2)
j=tkinter.Button(root,text=" 5 ",font=("bold",20),command=lambda:show(5),bg="grey",bd=5,width=2)
k=tkinter.Button(root,text=" 6 ",font=("bold",20),command=lambda:show(6),bg="grey",bd=5,width=2)
l=tkinter.Button(root,text=" 1 ",font=("bold",20),command=lambda:show(1),bg="grey",bd=5,width=2)
m=tkinter.Button(root,text=" 2 ",font=("bold",20),command=lambda:show(2),bg="grey",bd=5,width=2)
n=tkinter.Button(root,text=" 3 ",font=("bold",20),command=lambda:show(3),bg="grey",bd=5,width=2)
o=tkinter.Button(root,text=" * ",font=("bold",20),command=lambda:show("*"),bg="orange",bd=5,width=2)
p=tkinter.Button(root,text=" – ",font=("bold",20),command=lambda:show("-"),bg="orange",bd=5,width=2)
q=tkinter.Button(root,text=" + ",font=("bold",20),command=lambda:show("+"),bg="orange",bd=5,width=2)
r=tkinter.Button(root,text="      =      ",font=("bold",20),command=equal,bg="green",bd=5,width=8)
s=tkinter.Button(root,text=" 0 ",font=("bold",20),command=lambda:show(0),bg="grey",bd=5,width=2)
t=tkinter.Button(root,text=" . ",font=("bold",20),command=lambda:show("."),bg="grey",bd=5,width=2
                 )
b.place(x=60,y=90)
f.place(x=60,y=170)
i.place(x=60,y=270)
l.place(x=60,y=370)
t.place(x=60,y=470)
c.place(x=150,y=90)
g.place(x=150,y=170)
j.place(x=150,y=270)
m.place(x=150,y=370)
t.place(x=150,y=470)
d.place(x=250,y=90)
h.place(x=250,y=170)
k.place(x=250,y=270)
n.place(x=250,y=370)
s.place(x=60,y=470)
r.place(x=250,y=470)
e.place(x=350,y=90)
o.place(x=350,y=170)
p.place(x=350,y=270)
q.place(x=350,y=370)
root.mainloop()
