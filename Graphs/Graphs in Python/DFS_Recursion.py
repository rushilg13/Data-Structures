class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent = []
        self.visited = False

class DepthFirstSearch:
    def DFS(self, start):
        start.visited = True
        print(start.name, end = " -> ")

        for adj_node in start.adjacent:
            if adj_node.visited == False:
                self.DFS(adj_node)

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

breadthfirstsearch = DepthFirstSearch()
dfs = breadthfirstsearch.DFS(Node1)

# Output A -> B -> C -> D -> E -> F -> G -> H -> 