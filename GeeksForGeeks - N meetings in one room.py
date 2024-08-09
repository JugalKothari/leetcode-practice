class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meeting_pairs = [(start[i],end[i]) for i in range(n)]
        meeting_pairs.sort(key = lambda x: x[1])
        
        count=0
        last_end_time = -1
        for i in range(n):
            if meeting_pairs[i][0]>last_end_time:
                count+=1
                last_end_time=meeting_pairs[i][1]
        return count
