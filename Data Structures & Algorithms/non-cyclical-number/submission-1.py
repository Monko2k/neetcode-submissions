class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        while True:
            if num == 1:
                return True
            if num == 89: 
                return False
            
            numStr = str(num)
            new = 0
            for c in numStr:
                c_n = int(c)
                new += c_n ** 2
            num = new 

        