class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(i, m, cur):
            if i == 0 and m == 0:
                res.append(cur)
                return
            

            if i > 0:
                backtrack(i - 1, m + 1, cur + '(')
            if m > 0:
                backtrack(i, m - 1, cur + ')')

        backtrack(n, 0, '')
        return res

        