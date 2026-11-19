class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = [None] * len(nums)


        def dfs(i):
            if i >= len(nums) - 1: 
                return 0 
            if memo[i] is not None:
                return memo[i]
            num = nums[i]
            minJumps = math.inf
            for j in range(1, num + 1):
                minJumps = min(minJumps, 1 + dfs(i + j))
            memo[i] = minJumps 
            return minJumps
        
        
        return dfs(0)

        