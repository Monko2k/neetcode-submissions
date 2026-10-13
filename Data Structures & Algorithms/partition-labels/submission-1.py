class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occur = {}
        for i in range(len(s)):
            c = s[i]
            occur[c] = i + 1

        stringEnd = occur[s[0]]
        segLen = 0
        res = []
        for i in range(len(s)):
            c = s[i]
            if i == stringEnd:
                res.append(segLen)
                segLen = 1
                stringEnd = occur[c]
            else:
                last = occur[c]
                stringEnd = max(stringEnd, last)
                segLen += 1
        
        res.append(segLen)
        
        return res






        