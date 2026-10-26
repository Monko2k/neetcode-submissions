class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        last = [None] * (n + 1)
        for i in range(m, -1, -1):
            cur = [None] * (n + 1)
            for j in range(n, -1, -1):
                if i == m - 1 and j == n - 1:
                    cur[j] = 1
                    continue
                if i >= m or j >= n:
                    cur[j] = 0
                    continue

                res = cur[j + 1] + last[j]
                cur[j] = res
            last = cur

        return last[0]

            

        