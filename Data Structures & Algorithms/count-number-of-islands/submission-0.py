class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        MAX_ROW = len(grid)
        MAX_COL = len(grid[0])

        def bfs(start_x, start_y):
            stack = []
            stack.append((start_x, start_y))
            while stack:
                x, y = stack.pop()
                grid[x][y] = "x"
                if x > 0 and grid[x - 1][y] == "1":
                    stack.append((x - 1, y))
                if x < MAX_ROW - 1 and grid[x + 1][y] == "1":
                    stack.append((x + 1, y))
                if y > 0 and grid[x][y - 1] == "1":
                    stack.append((x, y - 1))
                if y < MAX_COL - 1 and grid[x][y + 1] == "1":
                    stack.append((x, y + 1))

        
        islands = 0
        
        for x, row in enumerate(grid):
            for y, item in enumerate(row):
                if item == "1":
                    islands += 1
                    bfs(x, y)
        return islands
        