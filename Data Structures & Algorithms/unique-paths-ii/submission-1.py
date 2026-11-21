class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        MAX_ROW = len(obstacleGrid) - 1
        MAX_COL = len(obstacleGrid[0]) - 1
        memo = [[None] * (MAX_COL + 1) for _ in range(MAX_ROW + 1)]

        def dfs(i, j):
            if obstacleGrid[i][j] == 1:
                return 0 
            if i == MAX_ROW and j == MAX_COL:
                return 1
            
            if memo[i][j] is not None:
                return memo[i][j]
            
            ways = 0
            if i + 1 <= MAX_ROW and obstacleGrid[i + 1][j] == 0:
                ways += dfs(i + 1, j)
            if j + 1 <= MAX_COL and obstacleGrid[i][j + 1] == 0:
                ways += dfs(i, j + 1)
            
            memo[i][j] = ways
            return ways
        
        return dfs(0, 0)
            


            



        