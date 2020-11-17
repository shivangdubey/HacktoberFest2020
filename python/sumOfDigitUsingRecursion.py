
# I/p: 1010
# o/p: 2

def sm(n):
  if n==0:
    return 0
    
  return n%10 + sm(n//10)


print(sm(1050))

