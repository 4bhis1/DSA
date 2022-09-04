#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:

        sum = num

        while(sum>9):

            temp = sum
            sum=0
            while(temp > 0):
                # print(temp%10,sum)
                sum = sum + temp%10
                temp = temp//10

        return sum



# @lc code=end

