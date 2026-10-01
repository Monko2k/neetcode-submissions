class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = [[None] * len(t) for _ in range(len(s))]

        def dfs(i, j):
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            if memo[i][j] is not None:
                return memo[i][j]

            char = s[i]
            target = t[j]
            ways = 0
            if char == target:
                ways += dfs(i + 1, j + 1)
            ways += dfs(i + 1, j)

            memo[i][j] = ways
            return ways
        
        return dfs(0, 0)



        