#Easy solution using itertools library
from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers="".join(str(i) for i in range(1, n+1))
        result=permutations(numbers)
        perms=["".join(p) for p in result]
        perms.sort()
        return perms[k-1]
        
