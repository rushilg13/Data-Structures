class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binary:
    def __init__(self, value):
        self.root = Node(value)
    
    def ancestor(self, node1, node2):
            
        pass

tree = binary(1)
tree.root.left = Node(2)
tree.root.right = Node(3)