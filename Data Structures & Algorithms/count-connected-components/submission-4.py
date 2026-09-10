class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return False

            if rank[rx] > rank[ry]:
                parent[ry] = rx
            elif rank[ry] > rank[rx]:
                parent[rx] = ry
            else:
                parent[ry] = rx
                rank[rx] += 1

            return True
        
        count = n
        for a, b in edges:
            if union(a, b):
                count -= 1
        return count

            
        

