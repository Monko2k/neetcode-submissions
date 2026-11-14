class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowAdj = defaultdict(list)
        rowDeg = defaultdict(int)
        colAdj = defaultdict(list)
        colDeg = defaultdict(int)
        for a, b in rowConditions:
            rowAdj[a].append(b)
            rowDeg[b] += 1
        
        for a, b in colConditions:
            colAdj[a].append(b)
            colDeg[b] += 1
        

        def kahn(adj, deg):
            order = {}
            idx = 0
            queue = deque()
            for i in range(1, k + 1):
                if deg[i] == 0:
                    queue.append(i)
            while queue:
                a = queue.popleft()
                order[a] = idx
                idx += 1
                for b in adj[a]:
                    deg[b] -= 1
                    if deg[b] == 0:
                        queue.append(b)
            return order
        
        rowOrder = kahn(rowAdj, rowDeg)
        colOrder = kahn(colAdj, colDeg)
        if len(rowOrder) != k or len(colOrder) != k:
            return []

        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            row = rowOrder[num]
            col = colOrder[num]
            matrix[row][col] = num
        return matrix


