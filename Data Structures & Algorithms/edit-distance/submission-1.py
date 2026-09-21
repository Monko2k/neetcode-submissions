class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[None] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        dp[len(word1)][len(word2)] = 0

        last = [0] * (len(word2) + 1)

        for i in range(len(word1), -1, -1):
            cur = [0] * (len(word2) + 1)
            for j in range(len(word2), -1, -1):
                
                if j == len(word2):
                    cur[j] = len(word1) - i
                    continue
    
                if i == len(word1):
                    cur[j] = len(word2) - j
                    continue
                
                c1 = word1[i]
                c2 = word2[j]
    
                res = []
                if c1 == c2:
                    res.append(last[j + 1])
                # insert
                res.append(1 + cur[j + 1])
                # replace
                res.append(1 + last[j + 1])
                # delete
                res.append(1 + last[j])
                minSteps = min(res)
                cur[j] = minSteps
            last = cur

        
        return last[0]

        