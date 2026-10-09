class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = [[None] * len(p) for _ in range(len(s))]

        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True
            
            if i == len(s):
                return j + 1 < len(p) and p[j + 1] == '*' and dfs(i, j + 2)
            if j == len(p):
                return False
            
            if memo[i][j] is not None:
                return memo[i][j]
            
            s_c = s[i]
            s_p = p[j]

            match = False
            if s_p == '.' or s_c == s_p:
                match |= dfs(i + 1, j + 1)
            if j < len(p) - 1 and p[j + 1] == '*':
                if s_p == '.' or s_c == s_p:
                    match |= dfs(i + 1, j)
                match |= dfs(i, j + 2)
            
            memo[i][j] = match
            return match
        
        return dfs(0, 0)




        