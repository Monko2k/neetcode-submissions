class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[-1]

        minSpeed = r
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            if hours > h:
                l = m + 1
            else:
                minSpeed = m
                r = m - 1
        
        return minSpeed



        