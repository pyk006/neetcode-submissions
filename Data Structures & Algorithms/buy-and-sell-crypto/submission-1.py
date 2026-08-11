class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0
        for i in range(1, len(prices)):
            curr_prof = prices[i] - prices[left]
            if prices[i] < prices[left]:
                left = i
            maxProfit = max(curr_prof, maxProfit)



        return maxProfit