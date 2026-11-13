class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowAdj = defaultdict(list)
        colAdj = defaultdict(list)
        rowDeg = defaultdict(int)
        colDeg = defaultdict(int)
        for a, b in rowConditions:
            rowAdj[a].append(b)
            rowDeg[b] += 1
        for a, b in colConditions:
            colAdj[a].append(b)
            colDeg[b] += 1
            
        def kahn(adj, deg):
            queue = deque()
            order = []
            for i in range(1, k + 1):
                if deg[i] == 0:
                    queue.append(i)

            while queue:
                a = queue.popleft()
                order.append(a)
                for b in adj[a]:
                    deg[b] -= 1
                    if deg[b] == 0:
                        queue.append(b)
            return order

        rowOrder = kahn(rowAdj, rowDeg)
        colOrder = kahn(colAdj, colDeg)
            
        if len(colOrder) != k or len(rowOrder) != k:
            return []

        rowIdx = {a: i for i, a in enumerate(rowOrder)}
        colIdx = {a: i for i, a in enumerate(colOrder)}
        
        
        arr = [[0] * k for _ in range(k)]
        
        for a in range(1, k + 1):
            i = rowIdx[a]
            j = colIdx[a]
            arr[i][j] = a
        
        return arr
            


        