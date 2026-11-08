class Solution:
    def totalNQueens(self, n: int) -> int:
        v_occ = [False] * n
        lr_occ = [False] * (2 * n - 1)
        rl_occ = [False] * (2 * n - 1)
        res = 0
        def dfs(i):
            nonlocal res
            if i == n:
                res += 1
                return
            for j in range(n):
                lr_idx = i + j
                rl_idx = i - j + n - 1
                if v_occ[j] or lr_occ[lr_idx] or rl_occ[rl_idx]: 
                    continue
                v_occ[j] = True
                lr_occ[lr_idx] = True
                rl_occ[rl_idx] = True
                dfs(i + 1)
                v_occ[j] = False
                lr_occ[lr_idx] = False
                rl_occ[rl_idx] = False

        dfs(0)

        return res
                







        