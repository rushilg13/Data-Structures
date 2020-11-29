class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop(-1)

class binary:
    def __init__(self, value):
        self.root = Node(value)
    
    def ancestor(self, node1, node2):
        if self.root == None:
            return
        if node1==self.root or node2 == self.root:
            print(self.root.value)
        if             

tree = binary(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.ancestor(tree.root,tree.root.left)