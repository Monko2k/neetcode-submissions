class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 - 1

        num = x
        res = 0
        while num != 0:
            digit = int(math.fmod(num,10))
            num = int(num / 10)
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10  or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit
        
        return res


        