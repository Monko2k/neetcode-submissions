"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        lastEnd = 0
        for interval in intervals:
            start = interval.start
            end = interval.end
            if lastEnd > start:
                return False
            lastEnd = end
        return True
