# https://leetcode.com/problems/remove-element/submissions/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        s=0
        e=len(nums)-1
        count=0
        
        while(s<=e):
            if(nums[s] == val):
                print(s,e)
                count=count+1
                
                nums[e],nums[s]=nums[s],nums[e]
                print(nums)
                # s=s+1
                e=e-1
            else:
                s=s+1
                
        print(nums, count)
                
        return len(nums)-count