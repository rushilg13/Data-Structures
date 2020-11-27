class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)

# This is How you unpack listed tuples in Python
# arr = [(1,2), (3,4), (5,6)]
# for i, j in arr:
#     print(i,j)
routes = [
            ("Mumbai", "Paris"),
            ("Mumbai", "Dubai"),
            ("Paris", "Dubai"),
            ("Paris", "New York"),
            ("Dubai", "New York"),
            ("New York", "Toronto"),
         ]

graph_routes = Graph(routes)