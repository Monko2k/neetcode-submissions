class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minString = None
        if len(s) < len(t):
            return ""
        tCounts = Counter(t)
        sCounts = defaultdict(int)
        l = 0
        r = 0
        matches = 0
        while True:
            if matches < len(t):
                if r == len(s):
                    break
                char = s[r]
                r += 1
                sCounts[char] += 1
                if tCounts[char] >= sCounts[char]:
                    matches += 1
            else:
                char = s[l]
                l += 1
                if tCounts[char] >= sCounts[char]:
                    matches -= 1
                sCounts[char] -= 1

            if matches == len(t) and (minString is None or (r - l) < (minString[1] - minString[0])):
                minString = (l, r)

        if minString is not None:
            l, r = minString
            return s[l:r]
        return ""
        