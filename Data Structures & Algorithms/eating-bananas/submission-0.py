class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        r = piles[-1]
        l = 1

        minSpeed = r

        while l <= r:
            m = (l + r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            if hours <= h:
                minSpeed = min(m, minSpeed)
                r = m - 1
            if hours > h:
                l = m + 1
            
        return minSpeed


    

        