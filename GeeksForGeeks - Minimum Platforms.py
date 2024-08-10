#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        times=[]
        for i in range(n):
            times.append([arr[i],'a'])
            times.append([dep[i],'d'])
            
        times.sort(key = lambda x: x[1])
        times.sort()
        plats=0
        max_plats=0
        for i in range(2*n):
            if times[i][1]=='a':
                plats+=1
            else:
                plats-=1
            max_plats = max(plats, max_plats)
        return max_plats
