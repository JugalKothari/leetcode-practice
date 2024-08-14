#User function Template for python3
class Solution:
	def maxSumIS(self, Arr, n):
	    maxSum=0
	    dp=[0]*(n)
	    for i in range(n):
	        dp[i]=Arr[i]
		  for i in range(1, n):
		      for j in range(i):
		          if Arr[j]<Arr[i]:
		              dp[i]=max(dp[i], dp[j] + Arr[i])
	    return max(dp)
