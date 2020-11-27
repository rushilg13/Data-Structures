class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent = []
        self.visited = False

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()

class BreadthFirstSearch:
    def BFS(self, start):
        queue = Queue()
        queue.enqueue(start)
        start.visited = True

        while len(queue)>0:
            node = queue.dequeue()
            print(node)
            if len(node.adjacent) > 0:
                for adj_node in node.adjacent:
                    if adj_node is False:
                        queue.enqueue(adj_node)
                        adj_node.visited = True







    
