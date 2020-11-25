# Binary Tree and Depth First Traversals
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder(self, start, traverse):
        if start:
            traverse += (str(start.value) + "->")
            traverse = self.preorder(start.left, traverse)
            traverse = self.preorder(start.right, traverse)
        return traverse
    
    def print_tree(self, traverse_type):
        if(traverse_type=="preorder"):
            return self.preorder(bin_tree.root, "") 
        elif(traverse_type=="inorder"):
            return self.inorder(bin_tree.root, "")
        elif(traverse_type=="postorder"):
            return self.postorder(bin_tree.root, "")
        else:
            return "Not a valid Traverse Type"

    def inorder(self, start, traverse):
        if start:
            traverse = self.inorder(start.left, traverse)
            traverse += str(start.value) + "->"
            traverse = self.inorder(start.right, traverse)
        return traverse
    
    def postorder(self, start, traverse):
        if start:
            traverse = self.postorder(start.left, traverse)
            traverse = self.postorder(start.right, traverse)
            traverse += str(start.value) + "->"
        return traverse



bin_tree = Tree(1)
bin_tree.root.left = Node(2)
bin_tree.root.right = Node(3)
bin_tree.root.left.left = Node(4)
bin_tree.root.left.right = Node(5)
bin_tree.root.right.left = Node(6)
bin_tree.root.right.right = Node(7)

print("Preorder Traversal:\n\t", bin_tree.print_tree("preorder") + "End\n")
print("Inorder Traversal:\n\t", bin_tree.print_tree("inorder") + "End\n")
print("Postorder Traversal:\n\t", bin_tree.print_tree("postorder") + "End\n")

# Our Tree Looks Like This
'''
                 1
              /    \
            2        3
          /   \    /   \
        4      5  6     7 
'''       