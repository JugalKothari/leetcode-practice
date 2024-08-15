#User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        def solve(arr, i, j):
            if i==j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            steps = float('inf')
            for k in range(i, j):
                product = arr[i-1]*arr[k]*arr[j]+solve(arr, i, k)+solve(arr, k+1, j)
                if product<steps:
                    steps=product
            dp[i][j]=steps
            return steps
    
        dp = [[-1]*N for i in range(N)]
        return solve(arr, 1, N-1)
