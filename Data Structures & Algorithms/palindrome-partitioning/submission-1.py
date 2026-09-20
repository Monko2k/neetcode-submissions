class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(arr):
            l = 0
            r = len(arr) - 1
            while l < r:
                if arr[l] != arr[r]:
                    return False
                l += 1 
                r -= 1 
            return True

        def dfs(i, palindromes, cur):
            if i == len(s):
                if len(cur) == 0:
                    res.append(palindromes.copy())
                return
            cur.append(s[i])
            if isPalindrome(cur):
                palindromes.append("".join(cur))
                dfs(i + 1, palindromes, [])
                palindromes.pop()
            
            dfs(i + 1, palindromes, cur)

        dfs(0, [], [])
        return res



            


        