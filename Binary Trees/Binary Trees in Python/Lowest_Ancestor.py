class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binary:
    def __init__(self, value):
        self.root = Node(value)


# INCOMPLETE!!!
# WILL COMPLETE LATER
# ISSEUES AND PULL REQUESTS APPRECIATED.
                      

tree = binary(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
#tree.ancestor(tree.root.right.right,tree.root.left.left)
