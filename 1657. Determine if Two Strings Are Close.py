class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1=Counter(word1)
        c2=Counter(word2)
        l1=list(c1.values())
        l1.sort()
        l2=list(c2.values())
        l2.sort()
        #Checking number of letters of an individual character
        if l1!=l2:
            return False
        l1=list(c1.keys())
        l1.sort()
        l2=list(c2.keys())
        l2.sort()
        #Checking if the characters present in the word are the same or not
        if l1!=l2:
            return False
        return True
