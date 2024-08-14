class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[0]*(len(word2)+1) for i in range(len(word1)+1)]

        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j]=j
        
        for index1 in range(1,len(word1)+1):
            for index2 in range(1,len(word2)+1):
                if word1[index1-1]==word2[index2-1]:
                    dp[index1][index2]=dp[index1-1][index2-1]
                else:
                    dp[index1][index2] = min(dp[index1][index2-1]+1,
                                                dp[index1-1][index2]+1,
                                                dp[index1-1][index2-1]+1)
        
        return dp[len(word1)][len(word2)]
        
