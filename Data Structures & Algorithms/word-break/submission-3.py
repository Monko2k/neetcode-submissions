class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None] * (len(s) + 1)

        def dfs(s, start, wordDict):
            if start == len(s):
                dp[start] = True
                return True
            if dp[start] != None:
                return dp[start]
            for word in wordDict:
                if s.startswith(word, start):
                    res = dfs(s, start + len(word), wordDict)
                    if res == True:
                        dp[start] = res
                        return res
            dp[start] = False
            return False
        
        dfs(s, 0, wordDict)
        return dp[0]

        