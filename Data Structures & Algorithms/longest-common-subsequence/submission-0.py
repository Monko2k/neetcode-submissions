class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1] * len(text2) for char in text1]
        print(memo)

        def dfs(i, j):

            if i == len(text1) or j == len(text2):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            if text1[i] == text2[j]:
                res = 1 + dfs(i + 1, j + 1)
                memo[i][j] = res
                return res
            res = max(dfs(i + 1, j), dfs(i, j + 1))
            memo[i][j] = res
            return res
        
        return dfs(0,0)
        

        