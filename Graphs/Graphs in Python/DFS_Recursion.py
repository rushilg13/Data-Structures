class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent = []
        self.visited = False

class DepthFirstSearch:
    def DFS(self, start):
        start.visited = True
        print(start.name)

        for adj_node in start.adjacent:
            if adj_node.visited == False:
                DFS(adj_node)