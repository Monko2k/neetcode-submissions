class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for a, b, t in times:
            adj[a].append((t, b))
        
        heap = [(0, k)]
        totalTime = 0
        visited = set()
        while heap:
            if len(visited) == n:
                return totalTime

            new_t, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            totalTime = new_t
            for t, b in adj[node]:
                heapq.heappush(heap, (totalTime + t, b))


        if len(visited) == n:
            return totalTime
        return -1
            


        