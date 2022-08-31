# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        
        res1 = [] 
        res2 = []
        
        max1=0
        max2=0
        
        for i,el in enumerate(height):
            
            max1=max([max1,el])
            res1.append(max1)
            
            max2=max([max2,height[len(height)-1-i]])
            res2.append(max2)
            
            
        res2=res2[::-1]
        
        ans = 0
        
        for i,el in enumerate(height) : 
            ans = ans + (min([res1[i],res2[i]])-el)

            
        return ans