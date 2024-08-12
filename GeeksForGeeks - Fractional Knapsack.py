#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        
        maxValueList=[]
        for i in range(n):
            valueperweight=arr[i].value/arr[i].weight
            maxValueList.append([valueperweight, arr[i].value, arr[i].weight])
        
        currweight=0
        currvalue=0.0
        maxValueList.sort(key = lambda x: x[0], reverse=True)
        for item in maxValueList:
            if currweight+item[2]<=w:
                currweight+=item[2]
                currvalue+=item[1]
            elif currweight<w:
                remweight=w-currweight
                currvalue+=(item[0]*remweight)
                currweight+=remweight
            else:
                break

        return currvalue
