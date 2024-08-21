class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        a=rounds[0]
        b=rounds[-1]
        if a<=b:
            return [i for i in range(a, b+1)]
        else:
            return [i for i in range(1, b+1)] + [i for i in range(a, n+1)]
