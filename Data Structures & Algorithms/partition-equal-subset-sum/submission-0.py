class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        maxSum = sum(nums)
        memo = [[None] * (maxSum + 1) for num in nums]

        def dfs(i, leftSum):
            rightSum = maxSum - leftSum
            if i == len(nums):
                return leftSum == rightSum
            if memo[i][leftSum] != None:
                return memo[i][leftSum]
            
            num = nums[i]
            res =  dfs(i + 1, leftSum + num) or dfs(i + 1, leftSum)
            memo[i][leftSum] = res
            return res
        
        return dfs(0, 0)

            
        