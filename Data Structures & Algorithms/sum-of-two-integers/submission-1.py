class Solution:
    def getSum(self, a: int, b: int) -> int:
        bitLength = 12
        sumRes = 0
        carry = 0
        for i in range(bitLength):
            ca = (a >> i) & 1
            cb = (b >> i) & 1

            res = ca ^ cb ^ carry
            newCarry = (ca & cb) | (carry & (ca ^ cb))
            carry = newCarry
            sumRes |= (res << i)
        
        if sumRes >> 11:
            sumRes |= (~0 << bitLength)
        return sumRes
            



        