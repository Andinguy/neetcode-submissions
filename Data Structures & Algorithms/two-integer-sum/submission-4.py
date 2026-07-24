class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for n in range(len(nums)):
            cmplt = target - nums[n]
            if cmplt in d:
                return [d[cmplt], n]
            d[nums[n]] = n
        return