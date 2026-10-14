class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr = 0
        for i in range(len(nums)):
            xorr ^= nums[i]
            xorr ^= i
        xorr ^= len(nums)
        return xorr
        