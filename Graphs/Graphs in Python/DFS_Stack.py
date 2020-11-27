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
    
    def size(size):
        return len(self.items)
    
class DepthFirstSearch:
    def DFS(self, start):
        stack = Stack()
        stack.push(start)
        print(start)
        start.visited = True

        while stack.size() > 0:
            node = stack.pop()
            if len(node.adjacent) > 0:
                for adj_node in node.adjacent:
                    stack.push(adj_node)
                    adj_node.visited = True


