class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(i, m, cur):
            if i == 0 and m == 0:
                res.append("".join(cur))
                return
            

            if i > 0:
                cur.append('(')
                backtrack(i - 1, m + 1, cur)
                cur.pop()
            if m > 0:
                cur.append(')')
                backtrack(i, m - 1, cur)
                cur.pop()

        backtrack(n, 0, [])
        return res

        