"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0

        start = []
        end = []

        for i in intervals:
            start.append(i.start)
            end.append(i.end)

        start.sort()
        end.sort()

        count = 0
        rooms = 0
        i = j = 0

        while i < len(intervals):

            if start[i] < end[j]:
                count += 1
                i += 1

            else:
                count -= 1
                j += 1

            rooms = max(rooms, count)

        return rooms