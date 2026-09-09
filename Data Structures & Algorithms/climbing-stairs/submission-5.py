class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [ 0 for _ in range(n)]
        mem[n - 1] = 1
        i = n - 2
        while i >= 0:
            if i + 2 >= n:
                mem[i] += 1
            else: 
                mem[i] += mem[i + 2]
            mem[i] += mem[i + 1]
            i -= 1


        return mem[0]
        