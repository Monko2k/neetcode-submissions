class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            nextMarker = s.find("#", i)
            len_s = int(s[i:nextMarker])
            i = nextMarker + 1
            res.append(s[i:i+ len_s])
            i += len_s
            
        return res
            




