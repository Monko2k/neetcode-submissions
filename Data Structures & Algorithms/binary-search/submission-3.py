class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            ptr = l + (r - l) // 2
            if nums[ptr] > target: 
                r = ptr - 1
            if nums[ptr] < target: 
                l = ptr + 1
            if nums[ptr] == target:
                return ptr
        return -1
        