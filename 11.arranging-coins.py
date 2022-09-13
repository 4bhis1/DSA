#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:

        i=1
        k=0

        while(i<=n and k<=n):
            if(k<n):
                i=i+1
            else:
                break
            k=k+i
            # print(k)

        return i-1


        
# @lc code=end

