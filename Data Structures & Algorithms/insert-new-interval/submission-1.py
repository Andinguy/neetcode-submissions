class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #base case: loop through by start and place after
        #overlapping case: take min start between overlap and take max end between overlap
        
        #merge case
        out = []
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                out.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                out.append(newInterval)
                return out + intervals[i:]
            else:
                newInterval = [min(intervals[i][0],newInterval[0]), max(intervals[i][1], newInterval[1])]
        out.append(newInterval)
        return out
        
