class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        curr = []
        res = []
        used = [False] * len(nums)
        nums.sort()

        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i, use in enumerate(used):
                if use: 
                    continue
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1]:
                    continue
                
                curr.append(nums[i])
                used[i] = True
                dfs()
                curr.pop()
                used[i] = False
        
        dfs()
        return res
            


        