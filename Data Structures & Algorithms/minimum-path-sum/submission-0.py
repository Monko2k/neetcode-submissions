class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        MAX_ROW = len(grid) - 1
        MAX_COL = len(grid[0]) - 1

        memo = [[None] * len(grid[0]) for _ in range(len(grid))]

        def dfs(i, j):
            if i == MAX_ROW and j == MAX_COL:
                return grid[i][j]
            
            if memo[i][j] is not None:
                return memo[i][j]
            
            right = math.inf
            down = math.inf
            if (i < MAX_ROW):
                right = dfs(i + 1, j)
            if (j < MAX_COL):
                down = dfs(i, j + 1)
            
            res = grid[i][j] + min(right, down)
            memo[i][j] = res
            return res
        
        return dfs(0, 0)

        