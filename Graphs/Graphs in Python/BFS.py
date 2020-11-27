class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent = []
        self.visited = False

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
