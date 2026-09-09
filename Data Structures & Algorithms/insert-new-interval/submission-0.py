class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        newStart, newEnd = newInterval
        lastInterval = len(intervals)

        for i, interval in enumerate(intervals):
            start, end = interval
            if end < newStart:
                res.append([start, end]) 
            elif start > newEnd:
                lastInterval = i
                break
            else:
                newStart = min(newStart, start)
                newEnd = max(newEnd, end)
        
        res.append([newStart, newEnd])
        for r in range(lastInterval, len(intervals)):
            res.append(intervals[r])
        return res



