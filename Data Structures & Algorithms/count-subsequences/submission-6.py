class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[None] * (len(t) + 1) for _ in range(len(s) + 1)]

        last = [None] * (len(t) + 1)

        for i in range(len(s), -1, -1):
            cur = [None] * (len(t) + 1)
            for j in range(len(t), -1, -1):
                if j == len(t):
                    cur[j] = 1
                    continue
                
                if i == len(s):
                    cur[j] = 0
                    continue
                
                char = s[i]
                target = t[j]
                ways = 0
                if char == target:
                    ways += last[j + 1]
                ways += last[j]
    
                cur[j] = ways
            last = cur
        
        return last[0]
