class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        iflags=[False]*len(matrix)
        jflags=[False]*len(matrix[0])
        for rowindex in range(len(matrix)):
            for colindex in range(len(matrix[rowindex])):
                if matrix[rowindex][colindex]==0:
                    iflags[rowindex]=True
                    jflags[colindex]=True
        for rowindex in range(len(matrix)):
            for colindex in range(len(matrix[rowindex])):
                if iflags[rowindex]or jflags[colindex]:
                    matrix[rowindex][colindex]=0
                    
        return matrix
        
