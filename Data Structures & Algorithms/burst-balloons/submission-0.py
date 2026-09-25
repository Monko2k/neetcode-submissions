class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = [[None] * len(nums) for _ in range(len(nums))]
        def dfs(l, r):
            if memo[l][r] is not None:
                return memo[l][r]
            maxVal = 0
            left = 1 if l == 0 else nums[l - 1]
            right = 1 if r == len(nums) - 1 else nums[r + 1]
            for i in range(l, r + 1):
                val = 0
                if i > l:
                    val += dfs(l, i - 1)
                if i < r:
                    val += dfs(i + 1, r)
                
                val += left * nums[i] * right

                maxVal = max(val, maxVal)
            memo[l][r] = maxVal
            return maxVal
        
        return dfs(0, len(nums) -1 )