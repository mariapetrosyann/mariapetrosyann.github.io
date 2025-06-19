class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_indexes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    zero_indexes.append((i, j))
        for i, j in zero_indexes:
            for col in range(len(matrix[0])):
                matrix[i][col] = 0
            for row in range(len(matrix)):
                matrix[row][j] = 0
        
