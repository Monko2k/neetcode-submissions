class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        deg = defaultdict(int)
        for a, b in prerequisites:
            adj[b].append(a)
            deg[a] += 1
        
        queue = deque()
        for i in range(numCourses):
            if deg[i] == 0:
                queue.append(i)
        
        finished = 0
        while queue:
            a = queue.popleft()
            finished += 1
            for b in adj[a]:
                deg[b] -= 1
                if deg[b] == 0:
                    queue.append(b)
        
        return finished == numCourses

        