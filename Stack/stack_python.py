# Building a stack using python list

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty() == True:
            return None
        else:
            return self.items.pop()
    
    def top_stack(self):
        if not self.is_empty():
            return self.items[-1]

# Testing
MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.items)

print(MyStack.top_stack())

MyStack.pop()
MyStack.pop()
print(MyStack.pop())