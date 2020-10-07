morsecode = {
    'A' : '. -', 'B' : '- . . .', 'C' : '- . - .', 'D' : '- . .',
    'E' : '.', 'F' : '. . - .', 'G' : '- - .', 'H' : '. . . .',
    'I' : '. .', 'J' : '. - - -', 'K' : '- . -', 'L' : '. - . .',
    'M' : '- -', 'N' : '- .', 'O' : '- - -', 'P' : '. - - .',
    'Q' : '- - . -', 'R' : '. - .', 'S' : '. . .', 'T' : '-',
    'U' : '. . -', 'V' : '. . . -', 'W' : '. - -', 'X' : '- . . -',
    'Y' : '- . - -', 'Z' : '- - . .', '1' : '. - - - -', '2' : '. . - - -',
    '3' : '. . . - -', '4' : '. . . . -', '5' : '. . . . .', '6' : '- . . . .',
    '7' : '- - . . .', '8' : '- - - . .', '9' : '- - - - .', '0' : '- - - - -',
    ',' : '- - . . - -', '.' : '. - . - . -', '?' : '. . - - . .', '/' : '- . . - .',
    '-' : '- . . . . -', '(' : '- . - - .', ')' : '- . - - . -',
}

def encrypt(message):
    new_message = ''
    for letter in message:
        if letter != ' ':
            new_message += morsecode[letter] + ' '*3
        else:
            new_message += ' '*7
    return new_message

def decrypt(message):
    message += ' '
    new_message = ''
    alpha = ''
    i = 0
    for letter in message:
        if letter != ' ':
            if i ==1:
                alpha += ' '
            i = 0
            alpha += letter
        else:
            i += 1
            if i == 3:
                new_message += list(morsecode.keys())[list(morsecode.values()).index(alpha)]
                alpha =''
            if i == 7:
                new_message += ' '
    return new_message


def welcome():
    print("\n\nHello Welcome to Morse code Translator")
    print("You have following options :")
    print("1: Morse-code to english text")
    print("2: English text to Morse-code")
    print("##### Please input your choice by the numbers 1 or 2 ###### ")
    print("##### Enter q to exit ######")


if __name__ == "__main__":
    welcome()
    while True:
        choice = input()
        if choice == 'q':
            print("Thanks for visiting!!!")
            break
        try:
            choice = int(choice)
            if choice == 1:
                print("Input your Morse-code")
                code = input()
                eng_text = decrypt(code.lower())
                print("Here's your english text")
                print(eng_text)
                welcome()
            if choice == 2:
                print("Input your english text")
                eng_text = input()
                code = encrypt(eng_text.upper())
                print("Here's your Morse-code")
                print(code)
                welcome()

        except Exception as e:
            print("Invalid choice please choose again!")
            print(e)


