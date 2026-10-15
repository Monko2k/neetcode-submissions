class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0
        r = 0
        maxLen = 0
        seen = {}
        while r < len(s):
            char = s[r]
            if char in seen:
                new_l = seen[char] + 1
                while l < new_l:
                    pop = s[l]
                    seen.pop(pop)
                    l += 1
            seen[char] = r
            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen



        