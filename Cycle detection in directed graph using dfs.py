class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        global_vis=[0]*numCourses
        local_vis=[0]*numCourses
        adj={i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        def dfs(node):
            if local_vis[node]==1:
                return False
            if global_vis[node]==1:
                return True
            global_vis[node]=1
            local_vis[node]=1
            for child in adj[node]:
                if not dfs(child):
                    return False
            local_vis[node]=0
            return True
        for course, prereq in prerequisites:
            if not dfs(course):
                return False
        return True
      
