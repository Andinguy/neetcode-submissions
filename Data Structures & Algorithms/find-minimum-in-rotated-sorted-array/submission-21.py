class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        out = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                out = min(out, nums[l])
                return out
            m = l + (r-l) // 2
            out = min(nums[m], out)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m -1

        return out
            
       

        
