class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        out = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            out = max(area, out)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return out