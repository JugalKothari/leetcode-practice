class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=m-1
        row=-1
        while left<right:
            mid=(left+right)//2
            if target<matrix[mid][-1]:
                right=mid
            elif target>matrix[mid][-1]:
                left=mid+1
            else:
                return True
        
        left=0
        row=right
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if target<matrix[row][mid]:
                right=mid-1
            elif target>matrix[row][mid]:
                left=mid+1
            else:
                return True
        return False
