class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seq = set()
        l = 0
        r = 0
        longest = 0
        while r < len(s):
            rChar = s[r]
            if rChar in seq:
                while rChar in seq:
                    lChar = s[l]
                    seq.remove(lChar)
                    l += 1
            
            seq.add(rChar)
            r += 1
            longest = max(longest, r - l)
        return longest



        