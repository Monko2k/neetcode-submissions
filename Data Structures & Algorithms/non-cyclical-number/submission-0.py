class Solution:

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquares(n)

        while slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
        
        return fast == 1



        
    

    def sumOfSquares(self, n):
        res = 0
        while n:
            digit = n % 10
            res += digit ** 2
            n = n // 10
        return res