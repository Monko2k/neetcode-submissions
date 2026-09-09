class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)

        def backtrack(cur, pick):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i, n in enumerate(nums):
                if not pick[i]:
                    cur.append(n)
                    pick[i] = True
                    backtrack(cur, pick)
                    cur.pop()
                    pick[i] = False
        backtrack([], pick)
        return res
            
        