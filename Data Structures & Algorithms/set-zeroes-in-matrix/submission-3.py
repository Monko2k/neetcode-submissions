class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row0 = False
        col0 = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                item = matrix[i][j]
                if item == 0:
                    if i == 0:
                        row0 = True
                    if j == 0:
                        col0 = True

                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if col0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
        
        