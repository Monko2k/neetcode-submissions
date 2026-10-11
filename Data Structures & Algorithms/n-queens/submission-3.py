class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queens = []
        colUsed = set()
        lrUsed = set()
        rlUsed = set()


        def backtrack(i):
            if i ==  n:
                rows = [("." * j + "Q" + "." * (n - j - 1)) for j in queens ]
                res.append(rows)
                return

            for j in range(n):
                lr = i - j
                rl = j + i
                if j not in colUsed and lr not in lrUsed and rl not in rlUsed:
                    colUsed.add(j)
                    lrUsed.add(lr)
                    rlUsed.add(rl)
                    row = "." * j + "Q" + "." * (n - j - 1)
                    queens.append(j)
                    backtrack(i + 1)
                    queens.pop()
                    colUsed.remove(j)
                    lrUsed.remove(lr)
                    rlUsed.remove(rl)
        
        backtrack(0)
        return res
            



        