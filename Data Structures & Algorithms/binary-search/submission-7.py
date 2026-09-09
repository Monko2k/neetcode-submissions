class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            pointer = l + ((r - l) // 2)
            val = nums[pointer]
            if val == target:
                return pointer
            if val > target:
                r = pointer - 1
            if val < target:
                l = pointer + 1
        return -1


        