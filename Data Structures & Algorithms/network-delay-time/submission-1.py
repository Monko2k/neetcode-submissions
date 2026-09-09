class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)
        for item in times:
            u, v, w = item
            adj[u].append((v, w))
        
        heap = [(0, k)]
        visited = set()
        time = 0
        while len(heap) > 0:
            w1, n1 = heapq.heappop(heap)
            if n1 in visited: 
                continue
            visited.add(n1)
            time = w1
            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(heap, (time + w2, n2))

        return time if len(visited) == n else -1