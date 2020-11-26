class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class Heap:
    def __init__(self, value):
        self.root = Node(value)
    


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


