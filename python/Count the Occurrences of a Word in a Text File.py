fname = input("Enter file name: ")
word = input("Enter word to be searched:")
k = 0
 
with open(fname, 'r') as f:
    f = f.lower()
    for line in f:
        words = line.split()
        for i in words:
            if(i==word):
                k=k+1
print("Occurrences of the word : ", end = "")
print(k)
