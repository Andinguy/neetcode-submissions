class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSub, maxSub = nums[0], nums[0]
        
        for n in nums[1:]:
            currSub = max(n, currSub + n)
            maxSub = max(currSub, maxSub)
        return maxSub