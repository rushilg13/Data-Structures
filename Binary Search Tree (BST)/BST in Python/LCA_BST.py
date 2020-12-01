class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, value):
        self.root = Node(value)
    
    def LCA(self, start, node1, node2):
        if(node1.value > start.value and node2.value > start.value):
            self.LCA(start.right, node1, node2)
        if(node1.value < start.value and node2.value < start.value):
            self.LCA(start.left, node1, node2)
        if(node1.value >= start.value and node2.value <= start.value):
            print(start.value)
        if(node1.value <= start.value and node2.value >= start.value):
            print(start.value)


tree = BST(100)
tree.root.left = Node(50)
tree.root.right = Node(110)
tree.root.left.left = Node(25)
tree.root.left.right = Node(75)
tree.root.right.left = Node(105)
tree.root.right.right = Node(120)
tree.LCA(tree.root, tree.root, tree.root.left)


'''
                100
             /      \
            50       110
          /    \    /   \
         25    75  105   120  
'''
