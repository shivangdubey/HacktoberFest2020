#finds the palindrome in one word

def palindrome(s, begin, end):
    while begin < end:
        if s[begin] != s[end]:
            return False
        begin+=1
        end-=1
    return True
    
word = input("input one word: ")
length = len(word)
if length > 1000:
    while length > 1000:
        print("input one word: ")
        word = input()
loop = length-1
count = 1
aux = loop
stop = 0
no = 0
for i in range (loop):
    for j in range(count):
        if palindrome(word, j, aux) is True:
            print (word[j:aux+1])
            stop = 1
            break
        aux = aux +1
    aux = loop - (i+1)
    if stop == 1:
        break
    count+=1
    no+=1
    if no == (loop):
        print("doesn't have a palindrome")
