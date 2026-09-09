class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1] * (len(s) + 1)

        def dfs(s, start, wordDict):
            if start == len(s):
                dp[start] = 1
                return 1
            if dp[start] != -1:
                return dp[start]
            for word in wordDict:
                if s[start:].startswith(word):
                    res = dfs(s, start + len(word), wordDict)
                    if res == 1:
                        dp[start] = res
                        return res
            dp[start] = 0
            return 0
        
        dfs(s, 0, wordDict)
        if dp[0] == 1:
            return True
        return False

        