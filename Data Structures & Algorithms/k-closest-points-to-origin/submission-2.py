class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            if len(heap) < k:
                heapq.heappush_max(heap, (dist, x, y))
            elif dist < heap[0][0]:
                heapq.heappop_max(heap)
                heapq.heappush_max(heap, (dist, x, y))


        return [[x, y] for _, x, y in heap]
        