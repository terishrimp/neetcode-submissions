class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyIndex = 0
        sellIndex = 0
        greatestDiff = 0
        for i in range(len(prices)):
            if prices[i] >= prices[sellIndex]:
                sellIndex = i
                greatestDiff = max(greatestDiff, prices[sellIndex]- prices[buyIndex])
            if prices[i] < prices[buyIndex]:
                buyIndex = i
                sellIndex = i
        
        print(f"buy at index {buyIndex}")
        print(f"sell at index {sellIndex}")
        print(f"greatestDiff {greatestDiff}")
        return greatestDiff
