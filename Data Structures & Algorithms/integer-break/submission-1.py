class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = i
            if i == n:
                dp[i] = 0
            for j in range(1, i):
                val = dp[j] * dp[i - j]
                dp[i] = max(dp[i], val)
        
        return dp[n]


        