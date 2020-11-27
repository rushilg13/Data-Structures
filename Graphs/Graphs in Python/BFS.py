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
Node4.adjacent.append(Node6)

'''
                          A
                      /   |  \   
                      B   F   G
                    /  \       \
                   C    D        H
                       /
                      E
'''

