class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [None] * len(nums)
        def dfs(i):
            if memo[i] is not None:
                return memo[i]
            best = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:                          # same check as `if num > n`
                    best = max(best, 1 + dfs(j))   # same as `include`
            memo[i] = best
            return best
        
        return max([dfs(i) for i in range(len(nums))])