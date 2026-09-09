class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(lambda: 0)
        heap = []
        for item in nums:
            freq[item] += 1
        
        for key, val in freq.items():
            if len(heap) == k:
                if heap[0][0] < val:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))


        return [ item[1] for item in heap ]
        