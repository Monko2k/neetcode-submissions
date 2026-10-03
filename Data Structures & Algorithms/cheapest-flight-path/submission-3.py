class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        edges = defaultdict(list)
        for u, v, c in flights:
            edges[u].append((v, c))

        heap = [(0, src, 0)]
        best_stops = {}
        while heap:
            cost, u, stops = heapq.heappop(heap)
            if u == dst:
                return cost
            if stops > k:
                continue
            if u in best_stops and best_stops[u] < stops:
                continue
            best_stops[u] = stops
            for v, c in edges[u]:
                heapq.heappush(heap, (c + cost, v, stops + 1))


        return -1
        