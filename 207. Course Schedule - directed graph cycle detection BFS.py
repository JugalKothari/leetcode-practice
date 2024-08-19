from queue import Queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        indegrees=[0]*numCourses
        for course, prereq in prerequisites:
            adj[course].append(prereq)
            indegrees[prereq]+=1
        q=Queue()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.put(i)
        processed_courses=0
        while not q.empty():
            course=q.get()
            processed_courses+=1
            for prereq in adj[course]:
                indegrees[prereq]-=1
                if indegrees[prereq]==0:
                    q.put(prereq)
        return processed_courses==numCourses
      
