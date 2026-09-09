class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        r = 0
        longest = 0

        while r < len(s):
            r_char = s[r]
            if r_char in seen and seen[r_char] >= l:
                l = seen[r_char] + 1
                seen[r_char] = r
            else:
                seen[r_char] = r
            
            longest = max(longest, r - l + 1)
            
            r += 1
        return longest

        