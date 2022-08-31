# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        temp = []
        count =0 
        for i in nums : 
            if (i!=0):
                temp.append(i)    
            else:
                count=count+1
                # nums.remove(0)
        
        for i in range(count):
            # temp.append(0)
            nums.remove(0)
            nums.append(0)
            
#         print(temp)
        
        # nums=temp
        
        # print(nums)
        """
        Do not return anything, modify nums in-place instead.
        """
        
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        s=0
        e=0
        
        while(e<len(nums)):
            
            if(nums[e] == 0):
                e=e+1
            else:
                nums[e],nums[s]=nums[s],nums[e]
                e=e+1
                s=s+1
            
        
        """
        Do not return anything, modify nums in-place instead.
        """
        