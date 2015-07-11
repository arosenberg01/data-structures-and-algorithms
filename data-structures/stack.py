# Implement a basic stack with methods:
#  push: add an item to the top of the stack
#  pop: remove the item at the top of the stack
#  peek: look at the item at the top of the stack without removing it
#  isEmpty: test if stack is empty or not
#  size: returns the number of items in the stack

class Stack():
    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.pop()

    def peek(self):
        return self.storage[len(self.storage) - 1]

    def size(self):
        return len(self.storage)

    def isEmpty(self):
        return self.storage == []
