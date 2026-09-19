class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        chars = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "qprs",
            '8': "tuv",
            '9': "wxyz",
        }

        res = []
        def dfs(i, cur):
            if i == len(digits):
                res.append("".join(cur))
                return
            
            char = digits[i]
            candidates = chars[char]

            for c in candidates:
                cur.append(c)
                dfs(i + 1, cur)
                cur.pop()
                
        dfs(0, [])
        return res
        