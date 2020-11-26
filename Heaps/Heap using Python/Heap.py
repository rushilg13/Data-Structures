class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def isEmpty(self):
        if(len(self.items==0)):
            return True
        else:
            return False

    def dequeue(self):
        if len(self.items)!=0:
            return self.items.pop()
    
    def peek(self):
        return self.items[-1].value
    
    def size(self):
        return len(self.items)
    
class Heap:
    def __init__(self, value):
        self.root = Node(value)
    
    def Levelorder(self, start, traversal):
        pass

    


heap = Heap(100)
heap.root.left = Node(40)
heap.root.left.left = Node(30)
heap.root.left.right = Node(20)
heap.root.right = Node(50)
heap.root.right.left = Node(40)
heap.root.right.right = Node(30)

'''
            100
           /    \
          40     50
        /   \   /  \
       30   20 40   30     

'''


