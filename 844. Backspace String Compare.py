class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        final_s=""
        final_t=""
        for ch in s:
            if ch=='#':
                final_s=final_s[:-1]
            else:
                final_s+=ch
        for ch in t:
            if ch=='#':
                final_t=final_t[:-1]
            else:
                final_t+=ch
        return final_s==final_t
        
