class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0: return 0 

        seen = {}
        l = 0
        r = l + 1
        seen[s[l]] = l

        maxLen = 1

        while r < len(s):
            char_r = s[r]
            if char_r in seen:
                l = max(l, seen[char_r] + 1)
            seen[char_r] = r
            
            maxLen = max(maxLen, r - l + 1)
            r += 1


        return maxLen

        