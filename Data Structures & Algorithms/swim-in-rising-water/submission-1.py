class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        MAX_ROW = len(grid) - 1
        MAX_COL = len(grid[0]) - 1
        

        visited = {(0, 0)}

        # val, i, j
        heap = [(grid[0][0], 0, 0)]


        level = 0
        while heap:
            val, i, j = heapq.heappop(heap)
            level = max(level, val)
            if i == MAX_ROW and j == MAX_COL:
                return level
            
            for d_i, d_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= d_i <= MAX_ROW and 0 <= d_j <= MAX_COL and (d_i, d_j) not in visited:
                    heapq.heappush(heap, (grid[d_i][d_j], d_i, d_j))
                    visited.add((d_i, d_j))
        




