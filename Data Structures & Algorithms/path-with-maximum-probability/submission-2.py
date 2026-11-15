class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            p = succProb[i]
            adj[a].append((b, p))
            adj[b].append((a, p))
        
        heap = [(-1, start_node)]
        visited = set()
        while heap:
            base, a = heapq.heappop(heap)
            base = -base
            if a == end_node:
                return base
            if a in visited:
                continue
            visited.add(a)

            for b, p in adj[a]:
                if b in visited:
                    continue
                new_p = base * p
                heapq.heappush(heap, (-new_p, b))

        return 0

        