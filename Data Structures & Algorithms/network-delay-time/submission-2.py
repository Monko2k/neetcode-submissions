class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, t in times:
            edges[u].append((t, v))
        

        visited = set()
        heap = [(0, k)]

        time = 0
        while heap:
            start_t, u = heapq.heappop(heap)
            if u in visited: 
                continue
            visited.add(u)
            time = max(time, start_t)
            for t, v in edges[u]:
                if v in visited:
                    continue
                
                heapq.heappush(heap, (start_t + t, v))

        if len(visited) != n:
            return -1
        
        return time


            

        