class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = set(c for w in words for c in w)
        if len(words) == 1:
            return ''.join(chars)

        dep = defaultdict(set)
        for i in range(1, len(words)):
            word0 = words[i - 1]
            word1 = words[i]

            firstMismatch = -1
            for j in range(len(word0)):
                if j >= len(word1):
                    return ""
                if word0[j] != word1[j]:
                    firstMismatch = j
                    break

            if firstMismatch == -1:
                continue
            c0 = word0[firstMismatch]
            c1 = word1[firstMismatch]
            dep[c0].add(c1)
        
        visited = set()
        path = set()
        res = []
        def dfs(c):
            if c in path:
                return True
            if c in visited: 
                return False
            visited.add(c)
            path.add(c)
            for v in dep[c]:
                val = dfs(v)
                if val:
                    return True
            path.remove(c)
            res.append(c)
            return False

        for c in chars:
            if dfs(c): 
                return ""
        
        res.reverse()
        return "".join(res)

        

      