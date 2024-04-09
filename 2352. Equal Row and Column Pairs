class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        originallen=len(grid)
        grid2=[]
        for i in range(originallen):
            newl=[]
            for j in range(originallen):
                newl.append(grid[j][i])
            grid2.append(newl)
        count=0
        i=0
        j=1
        while i<len(grid):
            list1=grid[i]
            for list2 in grid2:
                if list1==list2:
                    count+=1 
            i+=1
        return count
