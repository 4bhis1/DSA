#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prev = -1
        ans = 0
        for i,el in enumerate(prices) : 
            if(i > 0):
                if (prev<el):
                    ans = ans + el-prev
                prev = el
                
                print(ans)
                
            else:
                prev = el
        
        return ans