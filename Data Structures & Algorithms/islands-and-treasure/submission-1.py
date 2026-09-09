class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        MAX_X = len(grid)
        MAX_Y = len(grid[0])

        queue = deque()
        for x, row in enumerate(grid):
            for y, item in enumerate(row):
                if item == 0:
                    queue.append((x, y, 0))
        while queue:
            x, y, gen = queue.popleft()
            
            for dirr_x, dirr_y in [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1)
            ]:
                if (
                    dirr_x >= 0 
                    and dirr_x < MAX_X 
                    and dirr_y >= 0 
                    and dirr_y < MAX_Y 
                    and grid[dirr_x][dirr_y] == 2147483647
                ):
                    queue.append((dirr_x, dirr_y, gen + 1))
                    grid[dirr_x][dirr_y] = gen + 1
        








        