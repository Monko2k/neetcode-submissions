class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num: int) -> None:

        if len(self.minheap) == 0:
            self.minheap.append(num)
        elif self.minheap[0] < num:
            if len(self.minheap) > len(self.maxheap):
                old = heapq.heappop(self.minheap)
                heapq.heappush(self.minheap, num)
                heapq.heappush_max(self.maxheap, old)
            else:
                heapq.heappush(self.minheap, num)
        else:
            if len(self.maxheap) > len(self.minheap):
                old = heapq.heappop_max(self.maxheap)
                heapq.heappush_max(self.maxheap, num)
                heapq.heappush(self.minheap, old)
            else: 
                heapq.heappush_max(self.maxheap, num)

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + self.maxheap[0]) / 2
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return self.maxheap[0]
        
        