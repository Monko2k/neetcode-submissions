class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = defaultdict(set)
        for a, b in edges:
            connections[a].add(b)
            connections[b].add(a)
        

        count = n - len(connections)
        while len(connections) > 0:
            stack = []
            start = next(iter(connections))
            stack = list(connections.pop(start))
            count += 1
            while stack:
                key = stack.pop()
                if key not in connections:
                    continue
                stack += connections.pop(key)
        return count 
            





        