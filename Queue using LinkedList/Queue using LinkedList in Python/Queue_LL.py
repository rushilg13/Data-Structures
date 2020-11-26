class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue_LL:
    def __init__(self):
        self.start = None
    
    def enqueue(self, value):
        newNode = Node(value)
        newNode.next = self.start.next
        self.start = newNode
    
    