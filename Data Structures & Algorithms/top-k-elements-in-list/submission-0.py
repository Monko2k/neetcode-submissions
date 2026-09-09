class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(lambda: 0)
        for item in nums:
            freq[item] += 1

        heap = []
        heapq.heapify_max(heap)
        for key, value in freq.items():
            heapq.heappush_max(heap, (value, key))
        
        res = []
        for _ in range(k):
            value, key = heapq.heappop_max(heap)
            res.append(key)
        return res
        