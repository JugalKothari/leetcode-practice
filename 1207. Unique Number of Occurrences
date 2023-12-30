class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count=dict()
        for num in arr:
            if num not in count:
                count[num]=1
            else:
                count[num]+=1
        print(count)
        if len(count)==len(set(count.values())):
            return True
        else:
            return False
