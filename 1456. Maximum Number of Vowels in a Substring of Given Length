class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        maxvow=0
        isvowel=[ch in vowels for ch in s]
        maxvow=sum(isvowel[:k])
        if maxvow==k:
                return maxvow
        count=maxvow
        for i in range(k,len(s)):
            if isvowel[i-k]:
                count-=1
            if isvowel[i]:
                count+=1
            maxvow=max(count,maxvow)
            if maxvow==k:
                return maxvow
        return maxvow
