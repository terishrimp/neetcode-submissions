class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] >= prices[sell]:
                sell = i
                profit = max(profit, prices[sell]-prices[buy])
            elif prices[i] < prices[buy]:
                buy = i
                sell = i
        return profit
