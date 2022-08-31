# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        price=0
        
        for i in range(len(prices)-1,-1,-1):
            price = max([prices[i],price])
            ans = max([ans,price-prices[i]])
        
        return ans