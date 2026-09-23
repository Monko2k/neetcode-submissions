class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        chars = defaultdict(int)
        target = defaultdict(int)
        matches = 0
        for i in range(len(s1)):
            c1 = s1[i]
            target[c1] += 1

        for i in range(len(s1)):
            c2 = s2[i]
            if chars[c2] < target[c2]:
                matches += 1
            chars[c2] += 1

        if matches == len(s1):
            return True
        
        l = 0
        r = len(s1) - 1
        while r < len(s2) - 1:
            leftChar = s2[l]
            l += 1
            r += 1
            newChar = s2[r]
            if chars[leftChar] <= target[leftChar]:
                matches -= 1
            chars[leftChar] -= 1
            
            if chars[newChar] < target[newChar]:
                matches += 1
            chars[newChar] += 1

            if matches == len(s1):
                return True
        

        return False


