class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        connected = set()
        heap = [(0, (points[0][0], points[0][1]))]
        
        total = 0
        while heap:
            cost, b = heapq.heappop(heap)
            if b in connected:
                continue
            
            i, j = b
            connected.add(b)
            total += cost
            for d_i, d_j in points:
                if (d_i, d_j) in connected: 
                    continue
                
                newcost = abs(i - d_i) + abs(j - d_j)
                heapq.heappush(heap, (newcost, (d_i, d_j)))
                
        return total
            

        