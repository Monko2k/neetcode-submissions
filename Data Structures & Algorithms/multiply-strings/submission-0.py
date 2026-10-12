class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        n1 = num1[::-1]
        n2 = num2[::-1]

        for i1 in range(len(n1)):
            for i2 in range(len(n2)):
                d1 = ord(n1[i1]) - ord('0')
                d2 = ord(n2[i2]) - ord('0')
                total = d1 * d2 + res[i1 + i2]
                res[i1 + i2] = total % 10
                res[i1 + i2 + 1] += total // 10
        
        res.reverse()
        beg = 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        return ''.join(chr(ord('0') + c) for c in res[beg:])
