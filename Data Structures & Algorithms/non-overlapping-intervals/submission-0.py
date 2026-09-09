class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = None
        for start, end in intervals:
            if prevEnd == None or start >= prevEnd:
                prevEnd = end
            else:
                prevEnd = min(prevEnd, end)
                res += 1

        return res







        