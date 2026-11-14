"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        lastTime = 0
        for interval in intervals:
            lastTime = max(lastTime, interval.end)
        
        times = [0] * lastTime
        maxRooms = 0
        for interval in intervals:
            for i in range(interval.start, interval.end):
                times[i] += 1
                maxRooms = max(times[i], maxRooms)
        return maxRooms
        

        