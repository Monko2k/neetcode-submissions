class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowAdj = defaultdict(list)
        colAdj = defaultdict(list)
        for a, b in rowConditions:
            rowAdj[a].append(b)
        for a, b in colConditions:
            colAdj[a].append(b)
            
        def dfs(a, adj, state, order):
            if state.get(a, 0) == 1:
                return True
            if state.get(a, 0) == 2:
                return False
            state[a] = 1
            for b in adj[a]:
                if dfs(b, adj, state, order):
                    return True
            order.append(a)
            state[a] = 2
            return False

        colOrder = []
        colState = {}
        rowOrder = []
        rowState = {}

        for i in range(1, k + 1):
            if i not in rowState:
                if dfs(i, rowAdj, rowState, rowOrder):
                    return []
            if i not in colState:
                if dfs(i, colAdj, colState, colOrder):
                    return []
        rowOrder.reverse()
        colOrder.reverse()

        rowIdx = {a: i for i, a in enumerate(rowOrder)}
        colIdx = {a: i for i, a in enumerate(colOrder)}
        
        
        arr = [[0] * k for _ in range(k)]
        
        for a in range(1, k + 1):
            i = rowIdx[a]
            j = colIdx[a]
            arr[i][j] = a
        
        return arr
            


        