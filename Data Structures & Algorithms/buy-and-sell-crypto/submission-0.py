class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        lowest = prices[0]
        for num in prices:
            profit = num - lowest
            maxProfit = max(profit, maxProfit)
            lowest = min(lowest, num)
        return maxProfit
        