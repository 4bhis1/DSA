#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        s=1
        e=n
        ans = -1
        while(s<=e):
            mid = (s+e)//2

            if(isBadVersion(mid)):
                ans = mid
                e=mid-1
            else:
                s=mid+1
            
        return ans
        
# @lc code=end

