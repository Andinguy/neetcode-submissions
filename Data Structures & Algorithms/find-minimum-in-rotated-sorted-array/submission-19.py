class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ret = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                ret = min(nums[l], ret)
                return ret
            m = l + (r-l) // 2
            ret = min(nums[m], ret)

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return ret