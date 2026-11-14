from collections import defaultdict
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        deg = defaultdict(int)
        for a, neighbors in enumerate(graph):
            for b in neighbors:
                adj[b].append(a)
                deg[a] += 1
        
        queue = deque()
        for i in range(len(graph)):
            if deg[i] == 0:
                queue.append(i)
        
        safe = [False] * len(graph)
        while queue:
            a = queue.popleft()
            safe[a] = True
            for b in adj[a]:
                deg[b] -= 1
                if deg[b] == 0:
                    queue.append(b)
        
        res = []
        for i in range(len(graph)):
            if safe[i]:
                res.append(i)
        return res





