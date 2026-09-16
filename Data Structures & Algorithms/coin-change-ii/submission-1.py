class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[-1] * (amount + 1) for coin in coins]
        coins.sort()
        def dfs(i, amt):
            if i >= len(coins):
                return 0
            if memo[i][amt] != -1:
                return memo[i][amt]
            if amt == 0:
                return 1
            
            ways = 0
            if amt >= coins[i]:
                ways += dfs(i + 1, amt)
                ways += dfs(i, amt - coins[i])
            memo[i][amt] = ways
            return ways
        
        return dfs(0, amount)



        