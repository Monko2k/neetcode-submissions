class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[None] * len(word2) for _ in word1]

        def dfs(i, j):
            if j == len(word2) and i == len(word1):
                return 0
            
            if j == len(word2):
                return len(word1) - i

            if i == len(word1):
                return len(word2) - j
            
            if memo[i][j] != None:
                return memo[i][j]
            
            # char is correct
            c1 = word1[i]
            c2 = word2[j]

            res = []
            if c1 == c2:
                res.append(dfs(i + 1, j + 1))
            # insert
            res.append(1 + dfs(i, j + 1))
            # replace
            res.append(1 + dfs(i + 1, j + 1))
            # delete
            res.append(1 + dfs(i + 1, j))
            minSteps = min(res)
            memo[i][j] = minSteps

            return min(res)
        
        return dfs(0, 0)

        