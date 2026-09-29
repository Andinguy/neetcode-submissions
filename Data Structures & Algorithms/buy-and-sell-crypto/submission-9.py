class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        maxProf = 0
        while r < len(prices):
            currProf = prices[r] - prices[l]
            if prices[l] < prices[r]:
                maxProf = max(maxProf, currProf)
            else:
                l = r
            r += 1
        return maxProf
