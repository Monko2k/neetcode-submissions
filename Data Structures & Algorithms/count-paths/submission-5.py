class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                paths[j] = paths[j] + paths[j - 1]
            

        return paths[-1]
        