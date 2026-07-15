class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        greatestDiff = 0
        for i in range(len(prices)):
            for j in range(i + 1,len(prices),1):
                if prices[j] - prices[i] > greatestDiff:
                    print(f"{prices[j]-prices[i]}")
                    greatestDiff = prices[j] - prices[i]
        return greatestDiff