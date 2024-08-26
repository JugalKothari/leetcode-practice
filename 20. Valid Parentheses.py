class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={')':'(', '}':'{', ']':'['}
        stack=[]
        for ch in s:
            if ch in hashmap.values():
                stack.append(ch)
            elif not stack or stack.pop()!=hashmap[ch]:
                return False
        
        return not stack
        
