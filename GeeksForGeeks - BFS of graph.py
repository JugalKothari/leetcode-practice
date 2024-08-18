#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visited=[False]*V
        bfs_order=[]
        def bfs(node, adj, visited, bfs_order):
            q=Queue()
            q.put(node)
            visited[node]=True
            
            while not q.empty():
                node=q.get()
                bfs_order.append(node)
                
                for i in adj[node]:
                    if not visited[i]:
                        q.put(i)
                        visited[i]=True
            
        bfs(0, adj, visited, bfs_order)
        return bfs_order
