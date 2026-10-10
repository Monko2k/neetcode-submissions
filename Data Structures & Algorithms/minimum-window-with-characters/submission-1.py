class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minString = None
        if len(s) < len(t):
            return ""
        tCounts = Counter(t)
        sCounts = defaultdict(int)
        l = 0
        r = len(t)
        matches = 0
        for i in range(l, r):
            char = s[i]
            sCounts[char] += 1
            if char in tCounts and tCounts[char] >= sCounts[char]:
                matches += 1
            if matches == len(t) and (minString is None or (r - l) < len(minString)):
                minString = s[l:r]
        
        while True:
            if matches < len(t) and r < len(s):
                char = s[r]
                r += 1
                sCounts[char] += 1
                if char in tCounts and tCounts[char] >= sCounts[char]:
                    matches += 1
                if matches == len(t) and (minString is None or (r - l) < len(minString)):
                    minString = s[l:r]
            elif l + 1 < len(s):
                char = s[l]
                l += 1
                if char in tCounts and tCounts[char] >= sCounts[char]:
                    matches -= 1
                sCounts[char] -= 1
                if matches == len(t) and (minString is None or (r - l) < len(minString)):
                    minString = s[l:r]
            else:
                break

        if minString is not None:
            return minString
        return ""
        