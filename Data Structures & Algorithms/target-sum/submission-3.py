class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        maxTotal = sum(nums)
        size = (2 * maxTotal) + 1
        dp = [[0] * size for _ in range(len(nums) + 1)]
        for t in range(-maxTotal, maxTotal + 1):
            dp[len(nums)][t + maxTotal] = 1 if t == target else 0

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            for total in range(-maxTotal, maxTotal + 1):
                if i == len(nums):
                    continue
                ways = 0
                if -maxTotal <= total + num <= maxTotal:
                    ways += dp[i + 1][total + num + maxTotal]
                if -maxTotal <= total - num <= maxTotal:
                    ways += dp[i + 1][total - num + maxTotal]
                dp[i][total + maxTotal] = ways
                
        
        return dp[0][0 + maxTotal]