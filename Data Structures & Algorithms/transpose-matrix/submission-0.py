class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROW_SIZE = len(matrix[0])
        COL_SIZE = len(matrix)
        res = [[None] * COL_SIZE for _ in range(ROW_SIZE)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j][i] = matrix[i][j]
        return res
        