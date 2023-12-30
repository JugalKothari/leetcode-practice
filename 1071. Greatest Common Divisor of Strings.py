class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1=len(str1)
        n2=len(str2)
        s1=str1 if n1>n2 else str2
        s2=str2 if n1>n2 else str1
        i=len(s1)
        j=len(s2)
        gcd=0
        temp=0
        while j>=1:
            if i%j==0:
                gcd=j
                break
            else:
                temp=j
                j=i%j
                i=temp
        ans=""
        substr=s2[:gcd]
        j=len(substr)
        flag1=0
        while j>0:
            ans+=substr
            if ans==s1:
                flag1=1
                break
            elif len(ans)>len(s1):
                j=j-1
                substr=substr[:j]
                ans=""
        substr=s2[:gcd]
        j=len(substr)
        flag2=0
        ans=""
        while j>0:
            ans+=substr
            if ans==s2:
                flag2=1
                break
            elif len(ans)>len(s2):
                j=j-1
                substr=substr[:j]
                ans=""
        if flag1==1 and flag2==1: 
            return substr 
        else:
            return ""
