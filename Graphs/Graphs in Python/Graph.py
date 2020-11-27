class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph as a dictionary is:\n",self.graph_dict, end="\n\n")

# This is How you unpack listed tuples in Python
# arr = [(1,2), (3,4), (5,6)]
# for i, j in arr:
#     print(i,j)

    def Get_Paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:     # For Mumbai to Mumbai ie Same City to Same City
            return [path]
        
        if start not in self.graph_dict:  # For City which are not a starting point. like Toronto in eg
            return []
        
        paths = []
        
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.Get_Paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths


        



routes = [
            ("Mumbai", "Paris"),
            ("Mumbai", "Dubai"),
            ("Paris", "Dubai"),
            ("Paris", "New York"),
            ("Dubai", "New York"),
            ("New York", "Toronto"),
         ]

graph_routes = Graph(routes)
print("Paths between Mumbai and New York are:\n",graph_routes.Get_Paths("Mumbai", "New York"))