class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp = [[None] * (len(p) + 1) for _ in range(len(s) + 1)]

        for i in range(len(s), -1, -1):
            for j in range(len(p), - 1, - 1):
                if j == len(p):
                    dp[i][j] = i == len(s)
                    continue
                
                if i == len(s):
                    dp[i][j] = j + 1 < len(p) and p[j + 1] == '*' and dp[i][j + 2]
                    continue
                
                s_c = s[i]
                s_p = p[j]
    
                match = False
                if s_p == '.' or s_c == s_p:
                    match |= dp[i + 1][j + 1]
                if j + 1 < len(p) and p[j + 1] == '*':
                    if s_p == '.' or s_c == s_p:
                        match |= dp[i + 1][j]
                    match |= dp[i][j + 2]
                
                dp[i][j] = match
        
        return dp[0][0]




        