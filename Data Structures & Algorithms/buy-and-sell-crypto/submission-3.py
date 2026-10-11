class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        best = 0
        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            best = max(best, prices[right] - prices[left])
        
        return best