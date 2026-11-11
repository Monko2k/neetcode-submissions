class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1]
        for t in range(1, target + 1):
            dp.append(0)
            for num in nums:
                new_t = t - num
                if new_t >= 0:
                    dp[t] += dp[new_t]
        
        return dp[target]
        