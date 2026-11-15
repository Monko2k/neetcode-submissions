class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for a, b, c in flights:
            adj[a].append((c, b))
        
        heap = [(0, src, 0)]
        visited = {}
        while heap:
            cost, a, stops = heapq.heappop(heap)
            if a == dst:
                return cost
            if a in visited and visited[a] < stops or stops > k:
                continue
            visited[a] = stops
            for c, b in adj[a]:
                heapq.heappush(heap, (c + cost, b, stops + 1))
        
        return -1 
        