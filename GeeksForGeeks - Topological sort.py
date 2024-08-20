class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        visited=[False]*V
        order=[]
        def dfs(node, level):
            visited[node]=True
            order.insert(level, node)
            for child in adj[node]:
                if not visited[child]:
                    dfs(child, level+1)
        
        for starting in range(V):
            if not visited[starting]:
                dfs(starting, 0)
        
        return order
