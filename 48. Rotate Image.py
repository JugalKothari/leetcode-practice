class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for row in range(len(matrix)):
            for col in range(row,len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        return matrix
      
