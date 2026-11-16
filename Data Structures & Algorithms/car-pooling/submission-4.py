class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        L, R = math.inf, -math.inf
        for _, a, b in trips:
            L = min(L, a)
            R = max(R, b)

        N = R - L + 1
        points = [0] * N

        for n, a, b in trips:
            points[a - L] += n
            points[b - L] -= n
        
        curCapacity = 0
        for n in points:
            curCapacity += n
            if curCapacity > capacity:
                return False
        return True

        