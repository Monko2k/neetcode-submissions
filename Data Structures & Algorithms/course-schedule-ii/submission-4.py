class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        
        order = []
        visit = set()
        cycle = set()
        def dfs(a):
            if a in visit:
                return False
            if a in cycle:
                return True
            cycle.add(a)
            for b in adj[a]:
                if dfs(b):
                    return True
            order.append(a)
            cycle.remove(a)
            visit.add(a)
            return False




        for a in range(numCourses):
            if dfs(a):
                return []
        return order

        