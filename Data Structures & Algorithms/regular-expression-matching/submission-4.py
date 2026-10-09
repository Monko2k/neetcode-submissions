class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        last = [None] * (len(p) + 1)

        for i in range(len(s), -1, -1):
            cur = [None] * (len(p) + 1)
            for j in range(len(p), - 1, - 1):
                if j == len(p):
                    cur[j] = i == len(s)
                    continue
                
                if i == len(s):
                    cur[j] = j + 1 < len(p) and p[j + 1] == '*' and cur[j + 2]
                    continue
                
                s_c = s[i]
                s_p = p[j]
    
                match = False
                if s_p == '.' or s_c == s_p:
                    match |= last[j + 1]
                if j + 1 < len(p) and p[j + 1] == '*':
                    if s_p == '.' or s_c == s_p:
                        match |= last[j]
                    match |= cur[j + 2]
                
                cur[j] = match
            last = cur
        
        return last[0]




        