class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = defaultdict(int)
        for n, a, b in trips:
            points[a] += n
            points[b] -= n
        
        curCapacity = 0
        for point in sorted(points.keys()):
            curCapacity += points[point]
            if curCapacity > capacity:
                return False
        return True

        