class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        outList = defaultdict(list)

        for a, b in edges:
            outList[a].append(b)
            outList[b].append(a)
        
        visited = {0}
        stack = outList[0]

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            stack += outList[node]
        
        return n == len(visited)





        