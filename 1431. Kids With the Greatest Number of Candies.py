class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum=candies[0]
        for number in candies:
            if number>maximum:
                maximum=number
        answer=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=maximum:
                answer.append(True)
            else:
                answer.append(False)
        return answer
