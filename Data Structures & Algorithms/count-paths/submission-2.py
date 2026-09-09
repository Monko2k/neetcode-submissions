class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[ -1 for _ in range(n)] for _ in range(m)]

        queue = deque()
        queue.append((0,0))
        while queue:
            x, y = queue.popleft()
            if x == 0 and y == 0:
                grid[x][y] = 1
            elif grid[x][y] != -1:
                continue
            else:
                ways = 0
                if x > 0:
                    ways += grid[x - 1][y]
                if y > 0:
                    ways += grid[x][y - 1]
                grid[x][y] = ways
            for dir_x, dir_y in [(x + 1, y), (x, y + 1)]:
                if dir_x < m and dir_y < n:
                    queue.append((dir_x, dir_y))
        print(grid)
        
        return grid[m - 1][n - 1]


            
        