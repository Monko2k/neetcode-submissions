"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        overlaps = defaultdict(int)
        for interval in intervals:
            for i in range(interval.start, interval.end):
                overlaps[i] += 1
        
        return max(overlaps.values())
        