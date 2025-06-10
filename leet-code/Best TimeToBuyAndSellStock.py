class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        min_price_day = 0
        max_price = prices[min_price_day + 1]
        max_price_day = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                min_price_day = i
        for i in range(min_price_day + 1, len(prices)):
            if prices[i] > max_price:
                max_price = prices[i]
                max_price_day = i
        if max_price_day > min_price_day:
            profit = max_price - min_price
        return profit
