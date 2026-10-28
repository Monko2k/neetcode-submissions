class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sortTrips = sorted(trips, key=lambda x: x[1])
        heap = []
        c = 0
        position = 0
        for passengers, start, end in sortTrips:
            while heap and heap[0][0] <= start:
                _, p = heapq.heappop(heap)
                c -= p
            heapq.heappush(heap, (end, passengers))
            c += passengers
            if c > capacity:
                return False
        return True
        