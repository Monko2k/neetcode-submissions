class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = {}
        for c in s:
            if c in sFreq:
                sFreq[c] += 1
            else:
                sFreq[c] = 1

        tFreq = {}
        for c in t:
            if c in tFreq:
                tFreq[c] += 1
            else:
                tFreq[c] = 1
        
        return tFreq == sFreq
        
        