#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        sort = sorted(intervals,key = lambda x : x[0])
        print(sort)
        strt = sort[0][0]
        end = sort[0][1]
        ans = []
        for i in range(1,len(sort)):
            if(sort[i][0] <= end ):
                end=max(end,sort[i][1])
            else:
                ans.append([strt,end])
                strt = sort[i][0]
                end = sort[i][1]
            print(strt,end)

        ans.append([strt,end])

        return ans



# @lc code=end

