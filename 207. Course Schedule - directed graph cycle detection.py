from queue import Queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=[]
        adj={i:[] for i in range(numCourses)}
        indegrees=[0]*numCourses
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegrees[course]+=1
        q=Queue()
        for i in range(numCourses):
            if indegrees[i]==0:
                q.put(i)
        
        processed_courses=0
        while not q.empty():
            course=q.get()
            processed_courses+=1
            for dep in adj[course]:
                indegrees[dep]-=1
                if indegrees[dep]==0:
                    q.put(dep)
                    
        return processed_courses==numCourses
      
