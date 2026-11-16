class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seq = {}
        l = 0
        r = 0
        longest = 0
        while r < len(s):
            rChar = s[r]
            if rChar in seq:
                l = max(seq[rChar] + 1, l)
            seq[rChar] = r
            r += 1
            longest = max(longest, r - l)
        return longest



        