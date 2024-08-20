#Solution using dfs approach
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

#Solution using bfs approach
from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        visited=[False]*V
        order=[]
        indegrees=[0]*V
        for node in range(V):
            for adjacent in adj[node]:
                indegrees[adjacent]+=1
        
        q=deque()
        order=[]
        for node in range(V):
            if indegrees[node]==0:
                q.append(node)
                order.append(node)
                
        while q:
            node=q.popleft()
            for adjacent in adj[node]:
                indegrees[adjacent]-=1
                
                if indegrees[adjacent]==0:
                    q.append(adjacent)
                    order.append(adjacent)
        
        return order
