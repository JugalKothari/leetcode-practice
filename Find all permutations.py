class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers=[i for i in range(1, n+1)]
        def solve(numbers):
            result=[]
            if len(numbers)==1:
                return [numbers[:]]

            for i in range(len(numbers)):
                n=numbers.pop(0)
                perms=solve(numbers)
                for perm in perms:
                    perm.append(n)
                result.extend(perms)
                numbers.append(n)

            return result
        
        return solve(numbers)
