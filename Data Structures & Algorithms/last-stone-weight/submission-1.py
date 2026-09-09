class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = stones
        heapq.heapify_max(maxheap)
        while True:
            if len(maxheap) == 0: return 0
            if len(maxheap) == 1: return maxheap[0]
            x = heapq.heappop_max(maxheap)
            y = heapq.heappop_max(maxheap)
            if x != y:
                new = abs(x - y)
                heapq.heappush_max(maxheap, new)
        
        