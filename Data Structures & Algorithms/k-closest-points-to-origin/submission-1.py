class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = x**2 + y**2 
            if len(heap) < k:
                heapq.heappush_max(heap, (dist, [x, y]))
            elif heap[0][0] > dist:
                heapq.heappop_max(heap)
                heapq.heappush_max(heap, (dist, [x, y]))


        return [ i[1] for i in heap]

        