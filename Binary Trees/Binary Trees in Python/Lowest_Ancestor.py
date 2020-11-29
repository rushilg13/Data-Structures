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
    
    def peek(self):
        return self.items[-1]

class binary:
    def __init__(self, value):
        self.root = Node(value)
    
    def ancestor(self, node1, node2):
        if self.root == None:
            return
        if node1==self.root or node2 == self.root:
            print(self.root.value)
        else:
            stack1 = Stack()
            stack2 = Stack()
            temp1 = self.root
            # stack1.push(self.root)
            # stack2.push(self.root)
            while temp1 != node1 and temp1.left != None:
                stack1.push(temp1)
                temp1 = temp1.left
            temp1 = self.root
            while temp1 != node2 and temp1.left != None:
                stack2.push(temp1)
                temp1 = temp1.left
            if stack1.peek() == stack2.peek():
                print(stack1.peek().value)
            else:
                while stack1.peek() == stack2.peek():
                    stack1.pop()
                    stack2.pop()
                print(stack1.peek().value)
            

                      

tree = binary(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.ancestor(tree.root.left,tree.root.right)