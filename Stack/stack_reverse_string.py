class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return self.items == []
    
    def pop(self):
        if self.is_empty() == True:
            return None
        else:
            return self.items.pop()
    
    def top_stack(self):
        if not self.is_empty():
            return self.items[-1]

def reverse_str(str):
    s = Stack()
    
    for i in range(len(str)):
        s.push(str[i])
    rev_str = ''
    while not s.is_empty():
        rev_str += s.pop()
    
    return rev_str

str = "!dlrow ym ot emocleW"
print(reverse_str(str))