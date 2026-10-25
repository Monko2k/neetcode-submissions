class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = len(strs[0])
        for i in range(1, len(strs)):
            s = strs[i]

            ptr = 0
            n = min(len(strs[0]), len(s))
            while ptr < n and strs[0][ptr] == s[ptr]:
                ptr += 1
            
            common = min(common, ptr)
        
        return strs[0][:common]
        