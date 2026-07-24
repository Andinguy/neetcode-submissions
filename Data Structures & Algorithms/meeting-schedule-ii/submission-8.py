"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)

        s = e = 0

        count = res = 0

        while s < len(intervals):
            if start[s] >= end[e]:
                count -= 1
                e += 1
            else:
                s += 1
                count += 1
            res = max(count, res)
        return res