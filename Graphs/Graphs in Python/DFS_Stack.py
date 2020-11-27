class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent = []
        self.visited = False

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items[-1]
    
    def size(size):
        return len(self.items)
    
