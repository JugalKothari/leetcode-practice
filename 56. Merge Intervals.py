class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev=intervals[0]
        newintervals=[]
        for interval in intervals[1:]:
            if prev[1]>=interval[0]:
                endtime=max(prev[1],interval[1])
                prev=[prev[0],endtime]
            else:
                newintervals.append(prev)
                prev=interval
        newintervals.append(prev)
        return newintervals
