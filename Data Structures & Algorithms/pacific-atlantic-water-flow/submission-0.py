class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        MAX_ROW = len(heights) - 1
        MAX_COL = len(heights[0]) - 1
        reachPac = [[None for _ in heights[0]] for _ in range(len(heights))]
        reachAtl = [[None for _ in heights[0]] for _ in range(len(heights))]
        pacSet = set()

        atlSet = set()
        queue = deque()
        for x in range(len(heights)):
            queue.append((x, 0))
        for y in range(len(heights[0])):
            queue.append((0, y))

        while queue:
            x, y = queue.popleft()
            h = heights[x][y]
            reachPac[x][y] = True
            pacSet.add((x, y))
            
            for x_n, y_n in [
                (x + 1, y),
                (x - 1, y),
                (x , y + 1),
                (x , y - 1)
            ]:
                if x_n >= 0 and x_n <= MAX_ROW and y_n >= 0 and y_n <= MAX_COL:
                    if reachPac[x_n][y_n] != None:
                        continue
                    if heights[x_n][y_n] >= h:
                        queue.append((x_n, y_n))
            

        for x in range(len(heights)):
            queue.append((x, MAX_COL))
        for y in range(len(heights[0])):
            queue.append((MAX_ROW, y))
        while queue:
            x, y = queue.popleft()
            h = heights[x][y]
            reachAtl[x][y] = True
            atlSet.add((x, y))
            
            for x_n, y_n in [
                (x + 1, y),
                (x - 1, y),
                (x , y + 1),
                (x , y - 1)
            ]:
                if x_n >= 0 and x_n <= MAX_ROW and y_n >= 0 and y_n <= MAX_COL:
                    if reachAtl[x_n][y_n] != None:
                        continue
                    if heights[x_n][y_n] >= h:
                        queue.append((x_n, y_n))

        
        return list(pacSet & atlSet)

                

        