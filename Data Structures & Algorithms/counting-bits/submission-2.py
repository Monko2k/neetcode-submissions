class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0, 1, 1]
        if n < 3:
            return bits[:n + 1]
        for i in range(3, n + 1):
            if i & 1:
                bits.append(bits[i - 1] + 1)
            else:
                offset = i // 2
                bits.append(bits[offset])
        return bits
        