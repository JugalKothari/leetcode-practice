#Easy solution using itertools library
from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers="".join(str(i) for i in range(1, n+1))
        result=permutations(numbers)
        perms=["".join(p) for p in result]
        perms.sort()
        return perms[k-1]

#Math based solution
from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers=[]
        fact=1
        for i in range(1, n):
            numbers.append(i)
            fact*=i
        numbers.append(n)
        ans=""
        k-=1
        while True:
            ans+=str(numbers[k//fact])
            numbers.pop(k//fact)
            if not numbers:
                break
            k=k%fact
            fact=fact//len(numbers)
        return ans      
