class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        MAX_ROW = len(matrix) - 1
        MAX_COL = len(matrix[0]) - 1
        memo = [[None] * len(matrix[0]) for _ in range(len(matrix))]
        maxLength = 1
        def dfs(i, j):
            if memo[i][j] != None:
                return memo[i][j]
            val = matrix[i][j]

            longest = 1
            for i_n, j_n in [(i + 1, j), (i - 1, j), (i , j + 1), (i , j - 1)]:
                if 0 <= i_n <= MAX_ROW and 0 <= j_n <= MAX_COL:
                    val_n = matrix[i_n][j_n]
                    if val_n > val:
                        longest = max(1 + dfs(i_n, j_n), longest)
            memo[i][j] = longest
            return longest
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxLength = max(dfs(i, j), maxLength)
        
        return maxLength
                

        