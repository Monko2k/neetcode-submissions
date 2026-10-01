class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[None] * (len(t) + 1) for _ in range(len(s) + 1)]



        for i in range(len(s), -1, -1):
            for j in range(len(t), -1, -1):
                if j == len(t):
                    dp[i][j] = 1
                    continue
                
                if i == len(s):
                    dp[i][j] = 0
                    continue
                
                char = s[i]
                target = t[j]
                ways = 0
                if char == target:
                    ways += dp[i + 1][j + 1]
                ways += dp[i + 1][j]
    
                dp[i][j] = ways
        
        return dp[0][0]
