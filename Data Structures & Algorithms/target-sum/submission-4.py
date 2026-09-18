class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        maxTotal = sum(nums)
        size = (2 * maxTotal) + 1
        
        dp = [1 if t == target else 0 for t in range(-maxTotal, maxTotal + 1)]
        

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            cur_row = [0] * size
            for total in range(-maxTotal, maxTotal + 1):
                if i == len(nums):
                    continue
                ways = 0
                if -maxTotal <= total + num <= maxTotal:
                    ways += dp[total + num + maxTotal]
                if -maxTotal <= total - num <= maxTotal:
                    ways += dp[total - num + maxTotal]
                cur_row[total + maxTotal] = ways
            dp = cur_row
                
        
        return dp[maxTotal]
