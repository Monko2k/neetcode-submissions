class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def backtrack(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return
            num = nums[i]
            cur.append(num)

            backtrack(i + 1, cur)

            cur.pop()
            while (i < len(nums) and nums[i] == num):
                i += 1
            backtrack(i, cur)
        
        backtrack(0, [])
        return res



