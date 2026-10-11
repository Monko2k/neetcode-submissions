class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        diag = ((2 * n) - 1) # 7 
        offset = diag//2
        def backtrack(cur, colOpen, lrOpen, rlOpen):
            if len(cur) ==  n:
                res.append(cur.copy())
                return

            i = len(cur)
            for j in range(n):
                lr = i - j + offset
                rl = j + i
                if colOpen[j] and lrOpen[lr] and rlOpen[rl]:
                    colOpen[j] = False
                    lrOpen[lr] = False
                    rlOpen[rl] = False
                    row = "." * j + "Q" + "." * (n - j - 1)
                    cur.append(row)
                    backtrack(cur, colOpen, lrOpen, rlOpen)
                    cur.pop()
                    colOpen[j] = True
                    lrOpen[lr] = True
                    rlOpen[rl] = True
        
        backtrack([], [True] * n, [True] * diag, [True] * diag)
        return res
            



        