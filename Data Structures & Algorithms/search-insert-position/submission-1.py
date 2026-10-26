class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            val = nums[m]
            if val == target:
                return m
            elif val < target:
                l = m + 1
            else:
                r = m - 1



        return l
        