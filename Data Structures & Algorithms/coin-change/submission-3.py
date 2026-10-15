class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for amount in range(1, amount + 1):
            for c in coins:
                if amount - c >= 0:
                    dp[amount] = min(dp[amount], 1 + dp[amount - c])
        
        return dp[amount] if dp[amount] != math.inf else -1
