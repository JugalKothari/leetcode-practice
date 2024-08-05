class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n=len(A)
        sumA=sum(A)
        sumN=n*(n+1)//2
        A_N = sumA-sumN
        sumA2=0
        for i in range(n):
            sumA2+=A[i]**2
        sumN2 = (n * (n + 1) * (2 * n + 1)) // 6
        A2_N2 = sumA2 - sumN2
        AplusN = A2_N2 // A_N
        repeating = (A_N + AplusN) // 2
        missing = repeating - (A_N)
        return [int(repeating), int(missing)]
