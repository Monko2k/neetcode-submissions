class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        MAX_ROW = len(heights) - 1
        MAX_COL = len(heights[0]) - 1
        heap = [(0, 0, 0)]
        visited = set()
        while heap:
            diff, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if i == MAX_ROW and j == MAX_COL:
                return diff
            
            for di, dj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if ((di, dj) not in visited
                    and 0 <= di <= MAX_ROW
                    and 0 <= dj <= MAX_COL
                ):
                    curDiff = abs(heights[i][j] - heights[di][dj])
                    newDiff = max(curDiff, diff)
                    heapq.heappush(heap, (newDiff, di, dj))
        return 0 
            

        

        