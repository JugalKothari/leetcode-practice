#User function Template for python3
class Solution:
	def subsetSums(self, arr, n):
	    sums=[]
		def subsets(index, subseq):
		    if index==n:
		        sums.append(sum(subseq))
		        return
		    subseq.append(arr[index])
		    subsets(index+1, subseq)
		    subseq.pop()
		    subsets(index+1, subseq)
		
		subsets(0, [])
		return sums
    
