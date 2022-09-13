#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from cgi import MiniFieldStorage


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        strt=0
        end=len(nums)-1

        for i in range(0,len(nums)):
            if(i+1<len(nums)):
                print(">>",nums[i])
                if(nums[i] > nums[i+1]):
                    print("inside the condition")
                    if(target >= nums[0] and target <= nums[i]):
                        if(target == nums[0]):
                            return 0
                        elif(target == nums[i]):
                            return i
                        end=i
                    else:
                        strt = i +1
                        if(nums[i+1] == target):
                            return i+1
                    
                    break

        while(strt<=end):
            mid = (strt+end)//2
            if(nums[mid] == target):
                return mid
            elif (nums[mid]<target):
                strt = mid+1
            else:
                end= mid-1

        return -1


# @lc code=end

