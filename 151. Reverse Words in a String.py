class Solution:
    def reverseWords(self, s: str) -> str:
        l1=s.split()
        ans=[]
        for i in range(len(l1)):
            ans.append(l1[len(l1)-i-1])
        res=' '.join(ans)
        return res
