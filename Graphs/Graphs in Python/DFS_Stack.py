class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent = []
        self.visited = False

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
class DepthFirstSearch:
    def DFS(self, start):
        stack = Stack()
        stack.push(start)
        print(start.name)
        start.visited = True
        while stack:
            node = stack.pop()
            for adj_node in node.adjacent:
                if adj_node.visited==False:
                    stack.push(adj_node)
                    adj_node.visited = True


Node1 = Node("A")
Node2 = Node("B")
Node3 = Node("C")
Node4 = Node("D")
Node5 = Node("E")
Node6 = Node("F")
Node7 = Node("G")
Node8 = Node("H")

Node1.adjacent.append(Node2)
Node1.adjacent.append(Node6)
Node1.adjacent.append(Node7)
Node2.adjacent.append(Node3)
Node2.adjacent.append(Node4)
Node7.adjacent.append(Node8)
Node4.adjacent.append(Node5)

'''
                          A
                      /   |  \   
                      B   F   G
                    /  \       \
                   C    D        H
                       /
                      E
'''

depthfirstsearch = DepthFirstSearch()
dfs = depthfirstsearch.DFS(Node1)
# OUTPUT 
