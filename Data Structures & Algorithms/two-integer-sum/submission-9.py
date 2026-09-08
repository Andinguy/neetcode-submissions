class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            opp = target - n
            if opp in d:
                return [d[opp], i]
            else:
                d[n] = i
        return