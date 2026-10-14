class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #when you come across an overlap: the case where our current start time we are looking at 
        # is less than the prev end time, replace the end time at that time with the current
        intervals.sort(key = lambda i:i[0])

        out = [intervals[0]]
        

        for start, end in intervals[1:]:
            lastEnd = out[-1][1]
            if start <= lastEnd:
                out[-1][1] = max(lastEnd, end)
            else:
                out.append([start, end])
        return out
