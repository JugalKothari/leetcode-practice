class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        index1=len(text1)-1
        index2=len(text2)-1
        l1=list(text1)
        l2=list(text2)
        self.dp=[[-1] * len(text2) for i in range(len(text1))]
        answer = self.lcs(l1,l2,index1, index2)
        return answer

    def lcs(self, text1, text2, index1, index2):
        if index1==-1 or index2==-1:
            return 0
        if self.dp[index1][index2]!=-1: 
            return self.dp[index1][index2]
        if text1[index1]==text2[index2]:
            self.dp[index1][index2] = 1+self.lcs(text1, text2, index1-1, index2-1)
            return self.dp[index1][index2]
        self.dp[index1][index2] = 0+max(self.lcs(text1, text2, index1-1, index2), self.lcs(text1,text2, index1, index2-1))
        return self.dp[index1][index2]
