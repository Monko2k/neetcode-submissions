class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): 
            return False

        memo = [[None] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        def dfs(i, j):
            k = i + j
            if i == len(s1) and j == len(s2): 
                return k == len(s3)
            if memo[i][j] != None:
                return memo[i][j]


            if i < len(s1):
                char_1 = s1[i]
                char_3 = s3[k]
                if char_1 == char_3:
                    res = dfs(i + 1, j)
                    memo[i][j] = res
                    if res:
                        return True
            if j < len(s2):
                char_2 = s2[j]
                char_3 = s3[k]
                if char_2 == char_3 and dfs(i, j + 1):
                    res = dfs(i, j + 1)
                    memo[i][j] = res
                    if res:
                        return True

            memo[i][j] = False
            return False
        
        return dfs(0,0)

