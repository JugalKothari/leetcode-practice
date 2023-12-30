class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        l1=[]
        for char in s:
            if char in vowels:
                l1.append(char)
        s1=list(s)
        j=len(l1)
        for i in range(len(s1)):
            if s1[i] in vowels:
                s1[i]=l1[j-1]
                j-=1
        s=''.join(s1)
        return s
