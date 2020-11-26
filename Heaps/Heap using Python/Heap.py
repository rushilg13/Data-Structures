class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class Heap:
    def __init__(self, value):
        self.root = Node(value)
