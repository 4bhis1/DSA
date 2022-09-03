#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        # print(num)

        # num= 2

        binary=""

        while(num>0):
            binary = str( num%2)+binary
            num = num//2

        print(binary)

        complement = 0
        for i in range(len(binary)-1,-1,-1):
            if(binary[i]=='0'):
                # print(complement)
                complement=complement+2**(len(binary)-1-i)
        
        print(complement)

        return complement

        
# @lc code=end

