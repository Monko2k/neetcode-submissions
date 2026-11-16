class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        nums.sort()
        def dfs(i, t):
            if t == 0:
                res.append(cur.copy())
                return
            num = nums[i]
            new_t = t - num
            if new_t < 0:
                return
            cur.append(num)
            dfs(i, new_t)
            cur.pop()
            if i < len(nums) - 1:
                dfs(i + 1, t)
        
        dfs(0, target)
        return res



        