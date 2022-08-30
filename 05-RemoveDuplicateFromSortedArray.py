class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        obj = {}
        # length = len(nums)
        for i in nums : 
            obj[i]=1
            
        print(obj)
        
        let = []
        
        k=0
        for i in obj:
            # let.append(i)
            nums[k]=i
            k=k+1
        
        return len(obj)
        