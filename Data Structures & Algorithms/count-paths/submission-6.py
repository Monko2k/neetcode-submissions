class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[None] * n for _ in range(m)]


        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            if dp[i][j] is not None:
                return dp[i][j]
            
            res = dfs(i, j + 1) + dfs(i + 1, j)
            dp[i][j] = res
            return res

        return dfs(0, 0)

            

        