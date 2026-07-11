class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyPrice = prices[0]
        for sellPrice in prices:
            profit = max(profit, sellPrice - buyPrice)
            buyPrice = min(buyPrice, sellPrice)
        return profit