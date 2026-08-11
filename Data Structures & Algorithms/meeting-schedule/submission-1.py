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
        if len(intervals) == 0:
            return True
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if prev.end > intervals[i].start:
                return False
            prev = intervals[i]
        return True

