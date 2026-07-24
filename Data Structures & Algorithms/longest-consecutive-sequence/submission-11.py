class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # loop through
        #check if it the beginning of a sequence, keep track of maxCount of seq
        # repeat

        numSet = set(nums)
        maxCount = 0
        for n in nums:
            if n-1 not in numSet:
                count = 0
                while (n+count) in numSet:
                    count +=1
                maxCount = max(count,maxCount)
            
        return maxCount
        