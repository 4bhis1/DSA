#
# @lc app=leetcode id=1338 lang=python3
#
# [1338] Reduce Array Size to The Half
#

# @lc code=start
import enum


class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        collect = {}

        for i in arr:
            if(i in collect):
                collect[i]=collect[i]+1
            else:
                collect[i]=1


        sort = sorted(collect.items(),key = lambda x : x[1])

        i =len(sort)-1
        
        sum=0
        ans=0

        while(i>=0):
            sum=sum+sort[i][1]
            ans=ans+1

            if(sum>=len(arr)/2):
                break

            i=i-1

        return ans



        
# @lc code=end

