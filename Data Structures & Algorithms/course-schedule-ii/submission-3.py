class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        
        visited = {}
        order = []
        def dfs(a):
            if a in visited:
                if visited[a] == 1:
                    return True
                else:
                    return False
            visited[a] = 1
            for b in adj[a]:
                if dfs(b):
                    return True
            order.append(a)
            visited[a] = 2
            return False




        for a in range(numCourses):
            if dfs(a):
                return []
        return order

        