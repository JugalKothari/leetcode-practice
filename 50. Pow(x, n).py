import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            x=x**-1
            n=-1*n
        if n%2==1:
            return x * self.myPow(x, n-1)
        else:
            subans = self.myPow(x, n//2)
            return subans * subans
        
