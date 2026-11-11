class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        maxLen = mountainArr.length()

        l = 0 
        r = maxLen - 1
        pivot = 0
        while l <= r:
            m = l + (r - l) // 2
            left = mountainArr.get(m - 1)
            mid = mountainArr.get(m)
            right = mountainArr.get(m + 1)
            if left < mid and right < mid:
                pivot = m
                break
            elif left < mid < right:
                l = m + 1
            else:
                r = m - 1
        
        l = 0 
        r = pivot
        while l <= r:
            m = l + (r - l) // 2
            mid = mountainArr.get(m)
            if mid == target: 
                return m
            elif mid < target:
                l = m + 1
            else:
                r = m - 1

        l = pivot
        r = maxLen - 1
        while l <= r:
            m = l + (r - l) // 2
            mid = mountainArr.get(m)
            if mid == target: 
                return m
            elif mid > target:
                l = m + 1
            else:
                r = m - 1

        return -1 


            




        