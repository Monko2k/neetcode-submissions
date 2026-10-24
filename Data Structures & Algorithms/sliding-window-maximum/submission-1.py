class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = defaultdict(int)
        heap = []
        res = []
        l = 0
        r = 1
        while r <= len(nums):
            added = nums[r - 1]
            if r - l - 1 == k:
                removed = nums[l]
                window[removed] -= 1
                while heap and window[heap[0]] == 0:
                    heapq.heappop_max(heap)
                l += 1

            heapq.heappush_max(heap, added)
            window[added] += 1
            r += 1
            if r - l - 1 == k:
                res.append(heap[0])
        
        return res
