class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        max_gain=0
        while l<len(prices):
            for r in range(l+1,len(prices)):
                max_gain=max(max_gain,prices[r]-prices[l])
            l+=1
        return max_gain





    #         min_price=prices[0]
    #     max_profit=0
    #     for price in prices[1:]:
    #         min_price=min(min_price,price)
    #         max_profit=max(max_profit,price-min_price)
    #     return max_profit
    


    # max_gain=0

