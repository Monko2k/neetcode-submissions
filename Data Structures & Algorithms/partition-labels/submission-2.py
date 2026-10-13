class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occur = {}
        for i in range(len(s)):
            c = s[i]
            occur[c] = i

        stringEnd = occur[s[0]]
        segLen = 0
        res = []
        for i in range(len(s)):
            c = s[i]
            segLen += 1
            last = occur[c]
            stringEnd = max(stringEnd, last)

            if i == stringEnd:
                res.append(segLen)
                segLen = 0
        
        return res






        