class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal=[[1]]
        if numRows == 1:
            return pascal
        pascal.append([1,1])
        for i in range(2,numRows):
            row=[1]
            numindex=1
            while numindex<i:
                newnum=pascal[-1][numindex-1]+pascal[-1][numindex]
                row.append(newnum)
                numindex+=1
            row.append(1)
            pascal.append(row)
        return pascal
