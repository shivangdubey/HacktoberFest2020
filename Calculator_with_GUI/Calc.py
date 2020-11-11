from tkinter import *

def btnClick(number):
    global operator
    operator = operator + str(number)
    input_text.set(operator)

def btnClear(oper):
    global operator
    operator = ''
    input_text.set(operator)
    #       OR
    # text.delete(first=0,last=70)

def btnEquals(oper):
    global operator
    sumup = str(eval(operator))
    input_text.set(sumup)
    operator = ''


root = Tk()

root.title("calculator")
root.resizable(0,0)
operator = ''
root.config(background = 'orange')
input_text = StringVar()
root.geometry('447x522')


black1 = Label(root,bg = 'black',width = '65',height = '13')
black1.place(x = 0,y = 10)

calculator = Label(root,text='Calculator',bg='black',fg='orange',width='10',height='2',font = ('times',30,'bold','italic'))
calculator.place(x = 115,y = 10)

text = Entry(root,textvariable = input_text,bg = 'orange',fg = 'black',width = '24',font = ('times',25,'bold'),justify = 'right')
text.place(x = 16,y = 145)

black2 = Label(root,bg='black',width = '60',height = '19')
black2.place(x = 10,y = 220)

button7 = Button(root,text='7',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnClick(7),activebackground = 'orange')
button7.place(x = 13,y = 223)

button8 = Button(root,text='8',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnClick(8),activebackground = 'orange')
button8.place(x = 123,y = 223)

button9 = Button(root,text='9',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnClick(9),activebackground = 'orange')
button9.place(x = 233,y = 223)

buttonDivide = Button(root,text='/',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnClick('/'),activebackground = 'orange')
buttonDivide.place(x = 343,y = 223)

button4 = Button(root,text='4',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnClick(4),activebackground = 'orange')
button4.place(x = 13,y = 295)

button5 = Button(root,text='5',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnClick(5),activebackground = 'orange')
button5.place(x = 123,y = 295)

button6 = Button(root,text='6',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnClick(6),activebackground = 'orange')
button6.place(x = 233,y = 295)

buttonMultiply = Button(root,text='x',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnClick('*'),activebackground = 'orange')
buttonMultiply.place(x = 343,y = 295)

button1 = Button(root,text='1',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnClick(1),activebackground = 'orange')
button1.place(x = 13,y = 367)

button2 = Button(root,text='2',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnClick(2),activebackground = 'orange')
button2.place(x = 123,y = 367)

button3 = Button(root,text='3',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnClick(3),activebackground = 'orange')
button3.place(x = 233,y = 367)

buttonAdd = Button(root,text='+',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnClick('+'),activebackground = 'orange')
buttonAdd.place(x = 343,y = 367)

buttonClear = Button(root,text='C',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnClear('c'),activebackground = 'orange')
buttonClear.place(x = 13,y = 439)

button0 = Button(root,text='0',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnClick(0),activebackground = 'orange')
button0.place(x = 123,y = 439)

buttonEqual = Button(root,text='=',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnEquals('='),activebackground = 'orange')
buttonEqual.place(x = 233,y = 439)

buttonSub = Button(root,text='-',bg = 'black',fg = 'orange',width = '4',height = '1',font = ('times',25,'bold'),command = lambda:btnClick('-'),activebackground = 'orange')
buttonSub.place(x = 343,y = 439)

root.mainloop()