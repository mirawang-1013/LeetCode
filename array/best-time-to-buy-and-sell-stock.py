class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("infinity")
        max_profit=0
        for i in prices:
            if i< min_price:
                min_price = i
            else:
                max_profit = max(max_profit,i-min_price)
        return max_profit