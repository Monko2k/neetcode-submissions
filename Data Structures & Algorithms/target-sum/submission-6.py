class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        targetRange = (2 * totalSum) + 1
        memo = [[None] * targetRange for _ in range(len(nums))]

        def dfs(i, t):
            if i == len(nums):
                if t == 0:
                    return 1
                return 0
            if abs(t) > totalSum:
                return 0

            targetIndex = totalSum + t
            
            if memo[i][targetIndex] is not None:
                return memo[i][targetIndex]

            val = nums[i]
            res = dfs(i + 1, t + val) + dfs(i + 1, t - val)
            memo[i][targetIndex] = res
            return res

        return dfs(0, target)