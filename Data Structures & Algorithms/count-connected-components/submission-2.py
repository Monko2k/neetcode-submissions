class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return False
            parent[ry] = rx
            return True
        
        count = n
        for a, b in edges:
            if union(a, b):
                count -= 1
        return count

            
        

