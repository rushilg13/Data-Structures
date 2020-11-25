# Binary Tree and Depth First Traversals
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

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

class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder(self, start, traverse):
        if start:
            traverse += (str(start.value) + "->")
            traverse = self.preorder(start.left, traverse)
            traverse = self.preorder(start.right, traverse)
        return traverse
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
    
    def levelorder(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traverse = ""
        while queue.size()>0:
            traverse += str(queue.peek()) + "->"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traverse
    
    def reverse_levelorder(self, start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traverse = ""
        while queue.size()>0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        while stack.size()>0:
            node = stack.pop()
            traverse += str(node.value) + "->"
        return traverse

    
    def print_tree(self, traverse_type):
        if(traverse_type=="preorder"):
            return self.preorder(bin_tree.root, "") 
        elif(traverse_type=="inorder"):
            return self.inorder(bin_tree.root, "")
        elif(traverse_type=="postorder"):
            return self.postorder(bin_tree.root, "")
        elif(traverse_type=="levelorder"):
            return self.levelorder(bin_tree.root)
        elif(traverse_type=="reverse levelorder"):
            return self.reverse_levelorder(bin_tree.root)
        else:
            return "Not a valid Traverse Type"

    def height(self, node):
        if node == None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1+max(left_height, right_height)

    def size(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        count=1
        while queue.size()>0:
            node = queue.dequeue()
            if node.left:
                count+=1
                queue.enqueue(node.left)
            if node.right:
                count+=1
                queue.enqueue(node.right)
        print("Size of Tree is:",count)
    
    def check_bst(self, start):
        if start == None:
            return
        queue = Queue()
        queue.enqueue(start)
        while queue.size()>0:
            node = queue.dequeue()
            if(node.left):
                if(node.left.value < node.value and node.right.value > node.value):
                    queue.enqueue(node.left)
                    flag=1
                else:
                    flag=0
                    break
            if(node.right):
                if(node.left.value < node.value and node.right.value > node.value):
                    queue.enqueue(node.right)
                    flag=1
                else:
                    flag=0
                    break
        if(flag==1):
            print("Given Tree is a BST")
        else:
            print("Given Tree is not a BST")




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
print("Levelorder Traversal:\n\t", bin_tree.print_tree("levelorder") + "End\n")
print("Reverse Levelorder Traversal:\n\t", bin_tree.print_tree("reverse levelorder") + "End\n")

print("Max Height of Tree is", bin_tree.height(bin_tree.root))
bin_tree.size(bin_tree.root)
bin_tree.check_bst(bin_tree.root)
# Our Tree Looks Like This
'''
                 1
              /    \
            2        3
          /   \    /   \
        4      5  6     7 
'''       