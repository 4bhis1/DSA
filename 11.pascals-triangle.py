#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
from cgi import print_arguments


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ans = []

        for i in range(0,numRows):
            temp = []
            for j in range(0,i+1):
                # print(i,j)
                if (j==0):
                    temp.append(1)
                elif(j==i):
                    temp.append(1)
                else:
                    temp.append(ans[i-1][j-1]+ans[i-1][j])
                
                # print(temp)
            ans.append(temp)

        print(ans)

    
        return ans
        
# @lc code=end

