class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def rec(coins, amount, cache):
            if amount == 0:
                return 0
            if cache[amount - 1] != -2:
                return cache[amount - 1]
            valid = False
            minAmount = math.inf
            for coin in coins:
                if coin == amount:
                    return 1
                if coin < amount:
                    branch = rec(coins, amount - coin, cache)
                    if branch != -1:
                        valid = True
                        minAmount = min(minAmount, 1 + branch)
            if not valid:
                minAmount = -1
            cache[amount - 1] = minAmount
            return minAmount
        
        cache = [-2] * amount
        return rec(coins, amount, cache)

        



            




        