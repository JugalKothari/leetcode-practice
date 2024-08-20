from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited=[0]*len(graph)
        currcolor=1
        def bfs(node):
            if visited[node]==0:
                visited[node]=currcolor
                q=deque()
                q.append(node)
                while q:
                    node=q.popleft()
                    for nei in graph[node]:
                        if visited[nei]==0:
                            visited[nei]=-visited[node]
                            q.append(nei)
                        elif visited[nei]==visited[node]:
                            return False
            return True
                
        for starting in range(len(graph)):
            if not bfs(starting):
                return False
        return True
      
