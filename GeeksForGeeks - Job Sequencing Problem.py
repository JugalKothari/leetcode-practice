#User function Template for python3
'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''        

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        Jobs.sort(key = lambda x: x.profit, reverse=True)
        max_deadline = max(job.deadline for job in Jobs)
        slots=[False]*max_deadline
        jobs=0
        profit=0
        for job in Jobs:
            for j in range(job.deadline - 1, -1, -1):
                if not slots[j]:
                    jobs+=1
                    slots[j]=True
                    profit+=job.profit
                    break
                
        return [jobs, profit]
