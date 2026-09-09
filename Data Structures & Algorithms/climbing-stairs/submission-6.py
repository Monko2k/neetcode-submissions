class Solution:
    def climbStairs(self, n: int) -> int:
        oneAhead = 1
        twoAhead = 0
        for _ in range(n):
            temp = oneAhead + twoAhead
            twoAhead = oneAhead
            oneAhead = temp


        return oneAhead
        