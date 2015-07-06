# Implement a basic queue

class Queue():
    'Basic queue data structure'

    def __init__(self):
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)

    def dequeue(self):
        return self.storage.pop(0)
