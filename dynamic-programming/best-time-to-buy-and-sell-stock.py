class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        length=len(prices)
        for i in range(length):
            for j in range(i+1,length):
                if prices[j]>prices[i]:
                  max_profit=max(max_profit,prices[j]-prices[i])
        if max_profit>0:
            return max_profit
        else:
            return 0
    