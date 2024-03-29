class Solution:
    
    #Function to return list containing vertices in Topological order.
    def dfs(self, adj, stack, vis, curr):
        vis[curr] = True
        neigh = adj[curr]
        for i in neigh:
            if vis[i] == False:
                self.dfs(adj, stack, vis, i)
        stack.append(curr)
    
    def topoSort(self, V, adj):
        stack = []
        vis = [False for i in range(V)]
        for i in range(V):
            if vis[i] == False:
                self.dfs(adj, stack, vis, i)
        stack.reverse()
        return stack



#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)

# } Driver Code Ends
