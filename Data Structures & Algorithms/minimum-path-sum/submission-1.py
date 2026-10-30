class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        MAX_ROW = len(grid) - 1
        MAX_COL = len(grid[0]) - 1

        memo = [[None] * len(grid[0]) for _ in range(len(grid))]
        last = [None] * len(grid[0]) 

        for i in range(len(grid) - 1, -1, -1):
            cur = [None] * len(grid[0])
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == MAX_ROW and j == MAX_COL:
                    cur[j] = grid[i][j]
                    continue
                
                right = math.inf
                down = math.inf
                if (i < MAX_ROW):
                    right = last[j]
                if (j < MAX_COL):
                    down = cur[j + 1]
                
                res = grid[i][j] + min(right, down)
                cur[j] = res
            last = cur
        
        return last[0]

        