class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        maxTotal = sum(nums)
        size = (2 * maxTotal) + 1
        memo = [[None] * size for num in nums]


        def dfs(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if memo[i][total + maxTotal] != None:
                return memo[i][total + maxTotal]
            
            ways = 0
            num = nums[i]
            ways += dfs(i + 1, total + num)
            ways += dfs(i + 1, total - num)
            memo[i][total + maxTotal] = ways
            return ways
        
        return dfs(0, 0)


        