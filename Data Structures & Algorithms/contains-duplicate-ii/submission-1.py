class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 0
        window = set()
        while r < len(nums):
            val = nums[r]
            if r - l > k:
                lVal = nums[l]
                window.remove(lVal)
                l += 1
            if val in window: 
                return True
            window.add(val)
            r += 1
        
        return False
        