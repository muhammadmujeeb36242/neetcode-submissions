"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x: x.start)
        count = 1
        end = intervals[0].end
        for i in intervals[1:]:
            if i.start < end:
                return False
            end = i.end
        return True
