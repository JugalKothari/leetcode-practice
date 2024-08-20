from typing import List
class Solution:
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    def check_cyclic(node, adj, visited, parent)-> bool:
		    visited[node]=True
		    
		    for child in adj[node]:
		        if not visited[child]:
		            check_cyclic(child, adj, visited, node)
		        elif child!=parent:
		            return True
		    return False
		    
		for starting in range(V):
		    visited=[False]*V
		    if check_cyclic(starting, adj, visited, -1):
		        return True
		return False
