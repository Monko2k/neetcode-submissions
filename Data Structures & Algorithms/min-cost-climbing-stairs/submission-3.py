class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        oneAhead = 0
        twoAhead = 0
        for i in range(len(cost) - 1, -1, -1):
            cost_i = cost[i]
            minCost = min(oneAhead, twoAhead)
            temp = oneAhead
            twoAhead = oneAhead
            oneAhead = cost_i + minCost
        
        return min(oneAhead, twoAhead)


        