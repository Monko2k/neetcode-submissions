class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        chars_s = {}
        chars_t = {}

        for c in s:
            chars_s[c] = 1 + (chars_s.get(c, 0))

        for c in t:
            chars_t[c] = 1 + (chars_t.get(c, 0))

        return chars_s == chars_t
