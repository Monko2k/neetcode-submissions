class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1: return cost[0]
        if len(cost) == 2: return min(cost[0], cost[1])
        dp = [0] * (len(cost) + 1)
        #DP:    1 1 2 // 
        #COST:  1 2 3 // 
        for i in range(2, len(cost) + 1):
            oneStep = dp[i - 1] + cost[i - 1]
            twoStep = dp[i - 2] + cost[i - 2]
            dp[i] = min(oneStep, twoStep)

        return dp[len(cost)]
        
            