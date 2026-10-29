class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minVal = max(weights)
        maxVal = sum(weights)
        while minVal <= maxVal:
            m = (minVal + maxVal) // 2
            carried = 0
            d = 1
            for weight in weights:
                if carried + weight > m:
                    carried = weight
                    d += 1
                else:
                    carried += weight 
                
                if d > days:
                    break

            if d > days:
                minVal = m + 1
            else:
                maxVal = m - 1

        return minVal
        