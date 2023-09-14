#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:

        numbers = {'0' : 0,'1' : 1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        final = 0
        neg = False
        for i in s:
            if(i in numbers):
                final = final*10+numbers[i]
            elif i=='-' and final== 0 :
                neg = True

        return final*-1 if neg else final


        
# @lc code=end

