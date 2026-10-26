class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        last = [0] * (n + 1)
        for i in range(m - 1, -1, -1):
            cur = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    cur[j] = 1
                else:
                    cur[j] = cur[j + 1] + last[j]
            last = cur

        return last[0]

            

        