class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []


        def dfs(i, cur, t):
            if t == 0:
                res.append(cur.copy())
                return
            if i == len(candidates) or t < 0:
                return
            
            num = candidates[i]
            cur.append(num)
            dfs(i + 1, cur, t - num)
            cur.pop()

            while i < len(candidates) and candidates[i] == num:
                i += 1
            dfs(i, cur, t)

        dfs(0, [], target)
        return res


                


            
        