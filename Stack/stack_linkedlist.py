# Implementing a stack using Linked list'

# Add the Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Add the Stack class
class Stack:
    
    def __init__(self):
        self.head = None # No items in the stack, so head should be None
        self.num_elements = 0 # No items in the stack, so num_elements should be 0

    # Add the PUSH method
    def push(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head           # place the new node at the head of the linked list (top)
            self.head = new_node
        
        self.num_elements += 1

    # Adding the POP method
    def pop(self):
        if self.is_empty():
            return
        
        value = self.head.value # copy data to a local variable
        self.head = self.head.next # move head pointer to point to next node (top is removed by doing so)
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0