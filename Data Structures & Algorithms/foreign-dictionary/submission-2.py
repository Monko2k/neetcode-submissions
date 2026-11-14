class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        letters = set()
        for i in range(len(words)):
            for c in words[i]:
                letters.add(c)
            if i == 0: 
                continue
            w1 = words[i - 1]
            w2 = words[i]
            ci = 0
            while ci < len(w1) and ci < len(w2) and w1[ci] == w2[ci]:
                ci += 1
            
            if ci < len(w1) and ci < len(w2):
                c1 = w1[ci]
                c2 = w2[ci]
                adj[c2].append(c1)
            elif ci < len(w1):
                return ""
        
        order = []
        visited = set()
        cycle = set()

        def dfs(a):
            if a in visited:
                return False
            if a in cycle:
                return True
            cycle.add(a)
            for b in adj[a]:
                if dfs(b):
                    return True
            cycle.remove(a)
            visited.add(a)
            order.append(a)

        for c in letters:
            if dfs(c):
                return ""
            
        return ''.join(order)


        
            

        