from queue import Queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=[]
        adj={i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        def dfs(node, adj, visited):
            if node in visited:
                return False
            if adj[node]==[]:
                return True
            visited.append(node)
            for prereq in adj[node]:
                if not dfs(prereq, adj, visited):
                    return False
            adj[node]=[]
            visited.remove(node)
            return True
        for course, prereq in prerequisites:
            if not dfs(course, adj, visited):
                return False
        return True
