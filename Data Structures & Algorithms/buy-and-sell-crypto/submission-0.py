class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for price in prices[1:]:
            if price < buy:
                buy = price
            else:
                sell = price-buy
                profit = max(profit,sell)
        return profit