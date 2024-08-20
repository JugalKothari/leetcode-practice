class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited=[0]*len(graph)
        def dfs(node, currset):
            visited[node]=currset

            for child in graph[node]:
                if not visited[child]:
                    if not dfs(child, -currset):
                        return False
                elif visited[child]==visited[node]:
                    return False
            
            return True

        for starting in range(len(graph)):
            if not visited[starting]:
                if not dfs(starting, 1):
                    return False
        
        return True
      
