class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [math.inf] * n
        dist[src] = 0
        for i in range(k + 1):
            newDist = dist.copy()
            for a, b, c in flights:
                if dist[a] == math.inf:
                    continue
                newDist[b] = min(newDist[b], dist[a] + c)

            dist = newDist

        if dist[dst] == math.inf: 
            return -1
        return dist[dst]
        
        