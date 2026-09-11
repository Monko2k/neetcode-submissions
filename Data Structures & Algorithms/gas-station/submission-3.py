class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


        if sum(gas) < sum(cost):
            return -1
        
        bestStation = 0
        reserve = 0

        for i in range(len(gas)):
            reserve += (gas[i] - cost[i])
            if reserve < 0:
                reserve = 0
                bestStation = i + 1
        
        return bestStation

        