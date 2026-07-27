class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        out = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                out = min(nums[l], out)
                break
            m = l + (r-l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m -1
            out = min(nums[m], out)
        return out
