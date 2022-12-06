#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:

        arr = [1,2]

        def _fib(n):

            if(n< len):
                return arr[n]

            arr.append(_fib(n-1)+_fib(n-2))

            return arr[n]

        return _fib(n)
        
# @lc code=end

