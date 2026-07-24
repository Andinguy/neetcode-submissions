class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # loop through
        #check if it the beginning of a sequence, keep track of maxCount of seq
        # repeat

        maxCount = 0
        nums = set(nums)
        for n in nums:
            if (n-1) not in nums:
                count = 0
                while (n+count) in nums:
                    count +=1
                maxCount = max(maxCount, count)

        return maxCount