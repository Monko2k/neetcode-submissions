class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        MAX_X = len(grid)
        MAX_Y = len(grid[0])

        queue = deque()

        maxgen = 0 

        for x, row in enumerate(grid):
            for y, item in enumerate(row):
                if item == 2:
                    queue.append((x, y, 0))
        
        while queue:
            x, y, gen  = queue.popleft()
            for dir_x, dir_y in [
                (x + 1, y),
                (x - 1, y),
                (x, y - 1),
                (x, y + 1)
            ]:
                if (
                    dir_x >= 0
                    and dir_x < MAX_X
                    and dir_y >= 0
                    and dir_y < MAX_Y
                    and grid[dir_x][dir_y] == 1
                ):
                    grid[dir_x][dir_y] = 2
                    newgen = gen + 1
                    maxgen = max(newgen, maxgen)
                    queue.append((dir_x, dir_y, newgen))


        
        for x, row in enumerate(grid):
            for y, item in enumerate(row):
                if item == 1:
                    return -1

        return maxgen