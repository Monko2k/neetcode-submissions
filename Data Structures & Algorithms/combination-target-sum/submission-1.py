class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, s):
            if s == target:
                res.append(subset.copy())
                return
            if i == len(nums) or s > target:
                return

            num = nums[i]
            subset.append(num)
            dfs(i, s + num)

            subset.pop()
            dfs(i + 1, s)

            
        dfs(0, 0)
        return res
        