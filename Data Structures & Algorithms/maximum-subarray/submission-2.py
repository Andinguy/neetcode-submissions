class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        sub = nums[0]

        for n in nums[1:]:
            sub = max(n, sub + n)
            maxSub = max(sub, maxSub)
        return maxSub