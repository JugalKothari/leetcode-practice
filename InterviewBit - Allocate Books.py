class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def books(self, A, B):
        if B>len(A):
            return -1
        low=max(A)
        high=sum(A)
        def countstudents(mid):
            students=1
            pages=0
            for i in range(len(A)):
                if pages+A[i]<=mid:
                    pages+=A[i]
                else:
                    students+=1
                    pages=A[i]
            return students
        while low<=high:
            mid=(low+high)//2
            students=countstudents(mid)
            if students>B:
                low=mid+1
            else:
                high=mid-1
        return low
