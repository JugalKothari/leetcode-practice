#User function Template for python3
from typing import List
from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        indegrees=[0]*V
        for node in range(V):
            for dest in adj[node]:
                indegrees[dest]+=1
        q=deque()
        for node in range(V):
            if indegrees[node]==0:
                q.append(node)
        processed_nodes=0
        while q:
            node=q.popleft()
            processed_nodes+=1
            
            for adjacent in adj[node]:
                indegrees[adjacent]-=1
                
                if indegrees[adjacent]==0:
                    q.append(adjacent)
        return processed_nodes!=V
