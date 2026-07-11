class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for l in range(len(prices)):
            for r in range(l+1, len(prices)):
                if prices[l] < prices[r]:
                    profit = max(profit, prices[r] - prices[l])
                else:
                    continue
        return profit