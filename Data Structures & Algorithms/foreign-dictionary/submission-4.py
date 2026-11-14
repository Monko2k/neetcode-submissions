class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        deg = defaultdict(int)
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
                if c2 not in adj[c1]:
                    adj[c1].add(c2)
                    deg[c2] += 1
            elif ci < len(w1):
                return ""
        
        order = []
        queue = deque()
        for c in letters:
            if deg[c] == 0:
                queue.append(c)
            
        
        while queue:
            a = queue.popleft()
            order.append(a)
            for b in adj[a]:
                deg[b] -= 1
                if deg[b] == 0:
                    queue.append(b)
        
        if len(order) != len(letters):
            return ""

        return ''.join(order)


        
            

        