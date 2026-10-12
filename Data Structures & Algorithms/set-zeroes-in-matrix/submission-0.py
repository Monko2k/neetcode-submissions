class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZeroes = set()
        colZeroes = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                item  = matrix[i][j]
                if item == 0:
                    rowZeroes.add(i)
                    colZeroes.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rowZeroes or j in colZeroes:
                    matrix[i][j] = 0
        
        
        