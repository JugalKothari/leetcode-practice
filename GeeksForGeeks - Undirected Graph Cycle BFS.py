from typing import List
from queue import Queue
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visited=[False]*V
	    def check_cyclic(node, adj, visited):
	        q=Queue()
	        q.put((node, -1))
	        visited[node]=True
	        while not q.empty():
	            node, parent=q.get()
	            for adjacent in adj[node]:
	                if not visited[adjacent]:
	                    visited[adjacent]=True
	                    q.put((adjacent, node))
	                elif adjacent!=parent:
	                    return True
	        return False
	        
	    for starting in range(V):
	        if not visited[starting] and check_cyclic(starting, adj, visited):
	            return True
	    return False
