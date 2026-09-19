class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        def dfs(i, cur):
            if i == len(digits):
                res.append(cur)
                return
            
            candidates = ""
            char = digits[i]
            if char == '2':
                candidates = "abc"
            if char == '3':
                candidates = "def"
            if char == '4':
                candidates = "ghi"
            if char == '5':
                candidates = "jkl"
            if char == '6':
                candidates = "mno"
            if char == '7':
                candidates = "pqrs"
            if char == '8':
                candidates = "tuv"
            if char == '9':
                candidates = "wxyz"
            
            for c in candidates:
                dfs(i + 1, cur + c)
                
        dfs(0, "")
        return res
        