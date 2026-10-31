class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            val = arr[m]
            if val == x:
                l = m
                r = m + 1
                break
            elif val < x:
                l = m + 1
            else:
                r = m - 1
        
        l = min(l, r)
        r = l + 1
        for _ in range(k):
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            else:
                lDist = abs(arr[l] - x)
                rDist = abs(arr[r] - x)
                if rDist < lDist:
                    r += 1
                else:
                    l -= 1
        
        return arr[l + 1:r]
            
        

            
        