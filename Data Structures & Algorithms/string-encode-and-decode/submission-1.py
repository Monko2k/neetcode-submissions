class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s + "#"
        return res

    def decode(self, s: str) -> List[str]:
        countBuffer = ""
        res = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == "#":
                len_s = int(countBuffer)
                res.append(s[i + 1:i + 1 + len_s])
                i += len_s + 2
                countBuffer = ""
            else:
                countBuffer += c
                i += 1
            
        return res
            




