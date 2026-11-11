class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [None] * (target + 1)

        def dfs(t):
            if memo[t] is not None:
                return memo[t]
            ways = 0
            for num in nums:
                new_t = t - num
                if new_t == 0:
                    ways += 1
                elif new_t > 0:
                    ways += dfs(new_t)
            memo[t] = ways
            return ways

        return dfs(target)

        