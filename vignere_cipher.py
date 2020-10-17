def encrypt_fun(input_string,k):
    st=""
    for i in range(len(input_string)):
       if input_string.islower():
           shift=97    #ord(97)=a
       else:
           shift=65    #ord(65)=A
       s=(((ord(input_string[i]))+(ord(k[i])))%26)+shift
       st+=chr(s)
    return st

def key(length):
    t=list(input("Enter the key:"))
    s=""
    j=0
    while(len(s)!=length):
        s+=t[j]
        if j==len(t)-1:
            j=0
            continue
        j+=1
    return s

input_value=" "
while(input_value!="N"):
    print("=========================")
    print("Enter the message you want to encrypt:")
    input_string=input()
    k=key(len(input_string))
    encrypted_text=encrypt_fun(input_string,k)
    print("Encrypted Text :",encrypted_text)

    print("Do you want to encrypt again(Press N if not...and Press Y if yes..): ")
    input_value=input()
