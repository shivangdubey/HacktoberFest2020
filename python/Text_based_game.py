# imports
import time
import sys
import win32console

# This is a text based game in development
# You can type your commands, next steps etc. in the interface to get going

textSpeed=(0.1) #Sleep-Time between letters in Seconds [standard=0.1]
deniedWait=(1)  #Developer-Setting [standard=1]
password="general kenobi" #Access password [standard="1234"]

def init():
    access=False
    attempts=3
    print("Hello there! Please enter the Password:")
    while access==False:
        r1=input("Password:").lower()
        if r1==password:
            access=True
        elif attempts>1:
            attempts=attempts-1
            print("\nAccess denied! Try again (" + str(attempts) + " attemps remaining)")
        else:
            print("Access denied! Device locked for 30 Seconds")
            sec = 31    #seconds + 1
            digits = len(str(sec - 1))
            delete = "\b" * (digits)
            for i in range(sec):
                print("{0}{1:{2}}".format(delete, i, digits), end="")
                sys.stdout.flush()
                time.sleep(deniedWait)
            print()
    start()

def reden(s):
    for i in range(len(s)):
        sys.stdout.write(s[i])
        time.sleep(textSpeed)
        sys.stdout.flush()
    print()

def showHelp():
    reden("Is this your first time using µ-tech?")
    inp=input()
    if "yes" in inp.lower():
        reden("Ahh I see . . . So we'll start with the basics")
        basicHelp()
    elif "no" in inp.lower():
        reden("Oh . . . So why do you need help then?")
        advHelp(input())
    else:
        simpleInput(inp)

def basicHelp():
    pass

def advHelp(s):
    if "" in s.lower():
        pass                #case:1
    elif "" in s.lower():
        pass                #case:2
    else:
        simpleInput(s)      #case:default

def simpleInput(s):
    if "help" in s.lower(): showHelp()
    if "exit" in s.lower(): reden("System shutting down... See you soon"), exit()

def start():
    print("\nAccess granted!")
    print("Initialising script")
    loading()
    reden("Welcome to µ-tech")
    reden("What can I do for you? If you need help just ask for it")
    inp=input()
    simpleInput(inp)

def loading(lenght=20, speed=0.2):
    j=0
    for i in range(lenght):
        output_handle = win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
        info = output_handle.GetConsoleScreenBufferInfo()
        pos = info["CursorPosition"]
        a="/-\\|"
        output_handle.WriteConsoleOutputCharacter( a[j], pos )
        sys.stdout.write(".")
        time.sleep(speed)
        sys.stdout.flush()
        j=j+1
        if j==4: j=0
    print("\n")
    
init()
