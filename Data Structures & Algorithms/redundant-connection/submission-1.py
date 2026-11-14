class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return True
            if rank[root_a] < rank[b]:
                parent[root_a] = root_b
            elif rank[root_b] < rank[a]:
                parent[root_b] = root_a
            else:
                parent[root_b] = root_a
                rank[root_a] += 1

            return False
        
        for a, b in edges:
            if union(a, b):
                return [a, b]



        