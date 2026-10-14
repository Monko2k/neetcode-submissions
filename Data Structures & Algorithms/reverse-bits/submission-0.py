class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            flag = (n >> i) & 1
            res |= flag << (31 - i)
        return res

        