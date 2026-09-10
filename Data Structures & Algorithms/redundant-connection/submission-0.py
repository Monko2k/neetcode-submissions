class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [0] * (len(edges) + 1)

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rx = find(x)
            ry = find(y)

            if rx == ry:
                return True

            if rank[rx] > rank[ry]:
                parent[ry] = rx
            elif rank[ry] > rank[rx]:
                parent[rx] = ry
            else:
                parent[ry] = rx
                rank[rx] += 1
            return False
        
        for a, b in edges:
            if union(a, b):
                return [a, b]