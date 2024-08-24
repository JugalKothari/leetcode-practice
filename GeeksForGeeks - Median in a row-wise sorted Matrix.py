class Solution:
    def median(self, matrix, R, C):
        min_num=matrix[0][0]
        max_num=matrix[-1][-1]
        for i in range(R):
            min_num=min(min_num, matrix[i][0])
            max_num=max(max_num, matrix[i][-1])
        
        position = (R*C+1)//2
        
        def countsmallrow(arr, upperbound):
            low=0
            high=C-1
            while low<=high:
                mid=(low+high)//2
                if arr[mid]<=upperbound:
                    low=mid+1
                else:
                    high=mid-1
            return low
        
        def countsmall(mid):
            count=0
            for i in range(R):
                count+=countsmallrow(matrix[i], mid)
            return count
        
        while min_num<max_num:
            mid=(min_num+max_num)//2
            
            small=countsmall(mid)
            if small<position:
                min_num=mid+1
            else:
                max_num=mid
                
        return min_num
