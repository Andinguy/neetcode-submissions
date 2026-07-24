class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highestArea = 0
        l,r = 0, len(heights)-1
        while l<r:
            if heights[l] < heights[r]:
                Larea = heights[l]*(r-l)
                if Larea > highestArea:
                    highestArea = max(highestArea,Larea)
                l +=1

            else:
                Rarea = heights[r]*(r-l)
                if Rarea > highestArea:
                    highestArea = max(highestArea, Rarea)   
                r -=1
        return highestArea