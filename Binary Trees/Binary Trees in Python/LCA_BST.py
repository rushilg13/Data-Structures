class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, value):
        self.root = Node(value)

tree = BST(1)
tree.root.left = Node(2)
tree.root.right = Node(3)

