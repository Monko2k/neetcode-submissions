class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                adj[key].append(word)
        print(adj)
        
        seen = {beginWord}
        queue = deque([beginWord])
        generation = 0
        while queue:
            generation += 1
            for _ in range(len(queue)):
                item = queue.popleft()
                if item == endWord:
                    return generation
                for i in range(len(item)):
                    key = item[:i] + "*" + item[i + 1:]
                    for n in adj[key]:
                        if n not in seen:
                            queue.append(n)
                            seen.add(n)
        return 0
        
            

            



        