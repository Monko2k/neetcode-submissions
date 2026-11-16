class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        curSum = 0
        def dfs(i):
            nonlocal curSum
            if curSum == target:
                res.append(cur.copy())
                return
            if i == len(nums) or curSum > target:
                return
            num = nums[i]
            # add
            curSum += num
            cur.append(num)
            dfs(i)
            cur.pop()
            curSum -= num
            dfs(i + 1)
            return
        
        dfs(0)
        return res

            #skip



        