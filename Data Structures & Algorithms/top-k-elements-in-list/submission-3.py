class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(lambda: 0)
        for item in nums:
            freq[item] += 1
        
        buckets = [[] for _ in range(len(nums))]
        
        for key, val in freq.items():
            buckets[val - 1].append(key)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for item in buckets[i]:
                res.append(item)
                if len(res) == k:
                    return res
        return res

        