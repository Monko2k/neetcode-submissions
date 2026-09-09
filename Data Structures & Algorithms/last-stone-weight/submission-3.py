class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) > 1:
            stone1 = heapq.heappop_max(heap)
            stone2 = heapq.heappop_max(heap)

            if stone1 != stone2:
                val = stone1 - stone2
                heapq.heappush_max(heap, val)



        if len(heap) != 0:
            return heap[0]
        else:
            return 0
        