class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                out.append(newInterval)
                return out + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                out.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        out.append(newInterval)
        return out