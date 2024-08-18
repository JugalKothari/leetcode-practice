#User function Template for python3
class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited=[False]*V
        dfs_order=[]
        def dfs(node, adj, visited, dfs_order):
            visited[node]=True
            dfs_order.append(node)
            for i in adj[node]:
                if not visited[i]:
                    dfs(i, adj, visited, dfs_order)
                    
            return dfs_order
            
        return dfs(0, adj, visited, dfs_order)
      
