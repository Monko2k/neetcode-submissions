"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        s = sorted(intervals, key=lambda x: x.start)
        lastEnd = 0
        for item in s:
            start = item.start
            end = item.end
            if start < lastEnd:
                return False
            lastEnd = end

        return True

