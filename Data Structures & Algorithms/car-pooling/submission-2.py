class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        L = math.inf
        R = -math.inf
        for _, start, end in trips:
            L = min(L, start)
            R = max(R, end)
        
        N = R - L + 1
        diff = [0] * (N + 1)
        for p, s, e in trips:
            diff[s - L] += p
            diff[e - L] -= p
        
        c = 0
        for d in diff:
            c += d
            if c > capacity:
                return False
        
        return True

        