#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if(len(nums) == 1 and nums[0] == target):
            return [0,0]

        s=0
        e=len(nums)-1
        point = -1
        while(s<=e):
            mid = (s+e)//2
            if(nums[mid]>target):
                e=mid-1
            elif(nums[mid]<target):
                s=mid+1
            else:
                point=mid
                break
        
        # print("point",point)

        if(point == -1):
            return [-1,-1]

        li = []

        i=point

        while(i>=0):
            if(nums[i] != target):
                li.append(i+1)
                break
            elif(nums[i] == target and i ==0 ):
                li.append(i)
            
            print(nums[i],i)
            i=i-1

        i=point
        
        while(i<len(nums)):
            if(nums[i] != target):
                li.append(i-1)
                break
            elif(nums[i] == target and i == len(nums)-1):
                li.append(i)
            i=i+1

        return li
                

# @lc code=end

