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


def convert_int_to_bin(dec_num):
    
    if dec_num == 0:
        return 0
    
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    equi_bin = ""
    while not s.is_empty():
        equi_bin += str(s.pop())

    return equi_bin


#Testing

print(convert_int_to_bin(40))
print(int(convert_int_to_bin(56),2) == 56)