class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        substr=len(s)
        sent=len(t)
        i,j=0,0
        while i<substr and j<sent:
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i==substr:
            return True
        else:
            return False
