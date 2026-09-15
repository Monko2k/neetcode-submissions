class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[-1, -1] for _ in prices]
        


        def dfs(i, buy):
            if i >= len(prices):
                return 0
            idx = 0 if buy else 1     
            if memo[i][idx] != -1:
                return memo[i][idx]
            
            if buy:
                choose = dfs(i + 1, False) - prices[i]
                skip = dfs(i + 1, True)
                res = max(choose, skip)
                memo[i][idx] = res
                return res
            else:
                choose = prices[i] + dfs(i + 2, True)
                skip = dfs(i + 1, False)
                res = max(choose, skip)
                memo[i][idx] = res
                return res
        

        return dfs(0, True)
