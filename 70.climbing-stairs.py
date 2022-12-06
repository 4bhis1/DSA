#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:

        arr = []

        def _climbStairs(n) :

            if(n<0):
                return 0

            if(n==0):
                return 1

            if(n<len(arr)):
                return arr[n-1]

            arr.append(_climbStairs(n-1)+_climbStairs(n-2))

            return arr[n-1]

        return _climbStairs(n)


# @lc code=end

