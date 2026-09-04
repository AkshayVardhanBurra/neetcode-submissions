class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # pattern is a variable sliding window

        left = 0
        max_profit = 0

        for right in range(1, len(prices)):
            if prices[right] - prices[left] > max_profit:
                max_profit = prices[right] - prices[left]
            
            if prices[right] <= prices[left]:
                left = right
        
        return max_profit

        