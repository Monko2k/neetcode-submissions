class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]
        rank = [0] * len(isConnected)
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return

            if rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
            elif rank[root_b] < rank[root_a]:
                parent[root_b] = root_a
            else:
                parent[root_b] = root_a
                rank[root_a] += 1
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    union(i, j)
                
        
        return len(set(find(i) for i in range(len(isConnected))))


        