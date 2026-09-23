class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        chars = defaultdict(int)
        target = defaultdict(int)
        for i in range(len(s1)):
            target[s1[i]] += 1
            chars[s2[i]] += 1

        if chars == target:
            return True
        
        l = 0
        r = len(s1) - 1
        while r < len(s2) - 1:
            leftChar = s2[l]
            l += 1
            r += 1
            newChar = s2[r]
            chars[newChar] += 1

            chars[leftChar] -= 1
            if chars[leftChar] == 0:
                chars.pop(leftChar)

            if chars == target:
                return True
        

        return False


