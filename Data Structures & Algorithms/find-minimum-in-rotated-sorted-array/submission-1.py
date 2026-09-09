class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i == 0: 
                continue
            if n < nums[i - 1]:
                return n
        return nums[0]

        