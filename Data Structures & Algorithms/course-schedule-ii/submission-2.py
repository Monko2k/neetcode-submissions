class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        deg = defaultdict(int)
        for a, b in prerequisites:
            adj[b].append(a)
            deg[a] += 1
        
        queue = deque()
        for i in range(numCourses):
            if deg[i] == 0:
                queue.append(i)
        
        order = []
        while queue:
            a = queue.popleft()
            order.append(a)
            for b in adj[a]:
                deg[b] -= 1
                if deg[b] == 0:
                    queue.append(b)

        

        if len(order) != numCourses:
            return []
        
        return order

        