class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumNums = sum(nums)
        targetSum = 0
        for num in range(len(nums) + 1):
            targetSum += num
        return targetSum - sumNums
