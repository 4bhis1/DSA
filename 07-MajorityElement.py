class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        store = nums[0]
        count =1
        
        for i,el in enumerate(nums):
            if (i>0):
                if(count == 0):
                    store =el
                
                if(el == store):
                    count=count+1
                else:
                    count=count-1
                    
#         temp = 0
        
#         for i in nums:
#             if(i === store):
#                 temp=temp+1
                
#         if(temp > len(nums)/2):
            
        return store