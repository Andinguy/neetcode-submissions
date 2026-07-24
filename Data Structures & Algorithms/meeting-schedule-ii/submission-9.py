"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # Have 2 pters, 
        #if start time > end time --> decrement count move end ptr up one
        #if 
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)

        s = e = 0
        count = out = 0

        while s < len(intervals):
            if start[s] >= end[e]:
                count -= 1
                e += 1
            else:
                count += 1
                s += 1
        
            out = max(count, out)
        return out