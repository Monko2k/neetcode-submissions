class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        MAX_ROW = len(grid) - 1
        MAX_COL = len(grid[0]) - 1

        dp = [math.inf] * (len(grid[0]) + 1) 

        dp[MAX_COL] = 0

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):

                dp[j] = grid[i][j] + min(dp[j], dp[j + 1])
                
        return dp[0]

        