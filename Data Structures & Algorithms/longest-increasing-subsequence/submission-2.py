class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [None] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            best = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    best = max(best, 1 + memo[j])
            memo[i] = best
        
        return max(memo)