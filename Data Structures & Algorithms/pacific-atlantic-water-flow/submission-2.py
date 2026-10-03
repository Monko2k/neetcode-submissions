class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        MAX_ROW = len(heights) - 1
        MAX_COL = len(heights[0]) - 1

        reach_p = [[False] * len(heights[0]) for _ in range(len(heights))]
        queue = deque()
        for i in range(len(heights[0])):
            queue.append((0, i))
            reach_p[0][i] = True
        for i in range(1, len(heights)):
            queue.append((i, 0))
            reach_p[i][0] = True
        
        while queue:
            i, j = queue.popleft()
            val = heights[i][j]
            for d_i, d_j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if (0 <= d_i <= MAX_ROW 
                    and 0 <= d_j <= MAX_COL 
                    and reach_p[d_i][d_j] == False
                    and heights[d_i][d_j] >= val):
                    reach_p[d_i][d_j] = True
                    queue.append((d_i, d_j))

        visited = set()
        for i in range(len(heights[0])):
            queue.append((MAX_ROW, i))
            visited.add((MAX_ROW, i))
        for i in range(len(heights) - 1):
            queue.append((i, MAX_COL))
            visited.add((i, MAX_COL))

        res = []
        
        while queue:
            i, j = queue.popleft()
            if reach_p[i][j]:
                res.append([i, j])
            val = heights[i][j]
            for d_i, d_j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if (0 <= d_i <= MAX_ROW 
                    and 0 <= d_j <= MAX_COL 
                    and (d_i, d_j) not in visited
                    and heights[d_i][d_j] >= val):
                    queue.append((d_i, d_j))
                    visited.add((d_i, d_j))

        

        return res



                    




        