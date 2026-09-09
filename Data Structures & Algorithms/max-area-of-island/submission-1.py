class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        MAX_ROW = len(grid)
        MAX_COL = len(grid[0])
        maxArea = 0
        def dfs(start_x, start_y, mArea):
            area = 0
            stack = [(start_x, start_y)]
            while stack:
                x, y = stack.pop()
                if grid[x][y] == 1: 
                    area += 1
                    grid[x][y] = -1
                    for adj in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        adj_x, adj_y = adj
                        if adj_x >= 0 and adj_x < MAX_ROW and adj_y >= 0 and adj_y < MAX_COL:
                            stack.append(adj)
            return max(area, mArea)
        
        for x, row in enumerate(grid):
            for y in range(len(row)):
                maxArea = dfs(x, y, maxArea)

        return maxArea

                



        