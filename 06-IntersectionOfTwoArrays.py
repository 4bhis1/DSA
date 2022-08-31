# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        sets={}
        
        for i in nums1:
            if(i in sets):
                sets[i] =sets[i]+1
            else:
                sets[i]=1
            
        nums = []
        print(sets)
            
        for i in nums2:
            if(i in sets):
                if(sets[i]>0):
                    nums.append(i)
                    # del sets[i]
                    
                    sets[i]=sets[i]-1

                    print(sets)
                
        return nums