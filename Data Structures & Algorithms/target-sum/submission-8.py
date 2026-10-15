class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        if abs(target) > totalSum:
            return 0

        targetRange = (2 * totalSum) + 1
        dp = [[None] * targetRange for _ in range(len(nums) + 1)]
        
        for i in range(len(nums), -1, -1):
            for j in range(targetRange - 1, -1, -1):
                if i == len(nums):
                    if j == totalSum:
                        dp[i][j] = 1
                        continue
                    dp[i][j] = 0
                    continue

                val = nums[i]
                res = 0
                if j + val < targetRange:
                    res += dp[i + 1][j + val]
                if j - val >= 0:
                    res += dp[i + 1][j - val]
                dp[i][j] = res

        return dp[0][target + totalSum]