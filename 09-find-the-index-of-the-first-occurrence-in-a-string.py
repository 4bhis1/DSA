#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # try:
        #     return haystack.index(needle)
        # except:
        #     return -1

        # for i,el in enumerate(haystack):
        #     print(haystack[i:i+len(needle)])

        #     if(haystack[i:i+len(needle)] == needle):
        #         print(haystack[i:len(needle)])
        #         return i
        # return -1

        i =0
        prev = 0
        point =0
        bool = False
        while(i<len(haystack)):

            if(haystack[i] == needle[point]):
                point = point+1
                if(bool == False):
                    prev = i
                    print("inott hie")
                    bool = True
            else:
                point = 0
                # prev =0 
                if(bool == True):
                    i=prev
                    bool=False
                else:
                    prev = 0

            if(point == len(needle)):
                return prev

            print(point,prev,i+1)

            i=i+1
        
        return -1

        
# @lc code=end

