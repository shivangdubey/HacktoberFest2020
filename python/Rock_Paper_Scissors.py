from tkinter import *
from tkinter import messagebox
import random as r
def reset():
    global p1_choice,p2_choice
    b1['text']='Player 1 Roll'
    b1['state']=NORMAL
    p1.configure(image=general['player_1'])
    p1_choice=None
    b2['text']='Player 2 Roll'
    b2['state']=NORMAL
    p2.configure(image=general['player_2'])
    p2_choice=None
def compare():
    if((b1['text'][0]=='R' and b2['text']=='S') or (b1['text'][0]=='S' and b2['text']=='P') or (b1['text'][0]=='P' and b2['text']=='R')):
        messagebox.showinfo('Victory','Player 1 has Won.\n\tHurrah!!')
    elif(b1['text']==b2['text']):
        messagebox.showinfo('Draw',"Well that's a tie.\n\tBetter luck next time!!")
    else:
        messagebox.showinfo('Victory','Player 2 has Won.\n\tHurrah!!')
    reset()
def check():
    if(b1['state']==b2['state']==DISABLED):
        compare()
def p1_roll():
    global p1_choice
    p1_choice=r.choice(['rock','scissors','paper'])
    p1.configure(image=moves[p1_choice])
    b1['text']=p1_choice.title()
    b1['state']=DISABLED
    check()
def p2_roll():
    global p2_choice
    p2_choice=r.choice(['rock','scissors','paper'])
    p2.configure(image=moves[p2_choice])
    b2['text']=p2_choice.title()
    b2['state']=DISABLED
    check()
root=Tk()
root.title("Rock-Paper-Scissors")
font=(('Times New Roman','bold'),'20')
general={'player_1':PhotoImage(file='Assets/player1.png'),'player_2':PhotoImage(file='Assets/player2.png'),'vs':PhotoImage(file='Assets/vs.png')}
moves={'rock':PhotoImage(file='Assets/rock.png'),'paper':PhotoImage(file='Assets/paper.png'),'scissors':PhotoImage(file='Assets/scissor.png')}
f1=Frame(root)
p1=Label(f1,image=general['player_1'])
p1.pack(side='left')
vs=Label(f1,image=general['vs'])
vs.pack(side='left')
p2=Label(f1,image=general['player_2'])
p2.pack(side='left')
f1.pack()
f2=Frame(root)
b1=Button(f2,text='Player 1 Roll',width=20,font=font,command=p1_roll)
b1.pack(side='left')
f_space=Frame(f2,width=150)
f_space.pack(side='left')
b2=Button(f2,text='Player 2 Roll',width=20,font=font,command=p2_roll)
b2.pack(side='left')
f2.pack(pady=10)
p1_choice=None
p2_choice=None
root.mainloop()
