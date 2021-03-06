import heapq
import sys

class Edge:
    def __init__(self, weight, start, target):
        self.weight = weight
        self.start = start
        self.target = target

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacent = []
        self.minDist = sys.maxsize
    
    def __cmp__(self,other):
        return self.cmp(self.minDist, other.minDist)

    def __it__(self, other):
        selfPriority = self.minDist
        otherPriority = self.minDist
        return selfPriority < otherPriority

class Dijkstra:
    def CalculateShortestPath(self, vertexList, start):
        q=[]
        start.minDist = 0
        heapq.heappush(q, start)

        while len(q)>0:
            node = heapq.heappop(q)
            for edge in node.adjacent:
                u = edge.start
                v = edge.target
                newDist = u.minDist + edge.weight

                if newDist < v.minDist:
                    v.predecessor = u
                    v.minDist = newDist
                    heapq.heappush(q,v)

    def GetShortestPathTo(self, target):
        print("shortest path to vertex is", target.minDist)
        node = target
        while node is not None:
            print(node.name)
            node = node.predecessor

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

edge1 = Edge(5, node1, node2)
edge2 = Edge(8, node1, node5)
edge3 = Edge(9, node1, node5)
edge4 = Edge(15, node2, node4)
edge5 = Edge(12, node2, node3)
edge6 = Edge(4, node2, node8)
edge7 = Edge(7, node8, node3)
edge8 = Edge(6, node8, node6)
edge9 = Edge(5, node5, node8)
edge10 = Edge(4, node5, node6)
edge11 = Edge(20, node5, node7)
edge12 = Edge(1, node6, node3)
edge13 = Edge(13, node6, node7)
edge14 = Edge(3, node3, node4)
edge15 = Edge(11, node3, node7)
edge16 = Edge(9, node4, node7)

node1.adjacent.append(edge1)
node1.adjacent.append(edge2)
node1.adjacent.append(edge3)
node2.adjacent.append(edge4)
node2.adjacent.append(edge5)
node2.adjacent.append(edge6)
node8.adjacent.append(edge7)
node8.adjacent.append(edge8)
node5.adjacent.append(edge9)
node5.adjacent.append(edge10)
node5.adjacent.append(edge11)
node6.adjacent.append(edge12)
node6.adjacent.append(edge13)
node3.adjacent.append(edge14)
node3.adjacent.append(edge15)
node4.adjacent.append(edge16)

vertexList = (node1, node2, node3, node4, node5, node6, node7, node8)

dijkstra = Dijkstra()
dijkstra.CalculateShortestPath(vertexList, node1)
dijkstra.GetShortestPathTo(node7)

