class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        def expand_around_center(i, j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]
        max_str=s[0]
        for i in range(len(s)-1):
            odd = expand_around_center(i,i)
            even = expand_around_center(i,i+1)

            if len(odd)>len(max_str):
                max_str=odd
            if len(even)>len(max_str):
                max_str=even
        
        return max_str
        
