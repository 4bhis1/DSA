# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stck1 = []
        res1 = []
        
        for i,el in enumerate(heights):
            
            while(len(stck1)>0 and stck1[-1]["el"]>=el):
                stck1.pop()
                
            # print(stck1)
                
            if(len(stck1) == 0):
                res1.append(-1)
            elif(stck1[-1]["el"]<el):
                res1.append(stck1[-1]["in"])
                
            stck1.append({"el":el,"in":i})
            
        # print(res1)
        
        stck2 = []
        res2 = []
        
        for i in range(len(heights)-1,-1,-1):
            
            while(len(stck2)>0 and stck2[-1]["el"]>=heights[i]):
                stck2.pop()
                
            if(len(stck2) == 0 ):
                res2.append(len(heights))
            elif(stck2[-1]["el"]<heights[i]):
                res2.append(stck2[-1]["in"])

            stck2.append({"el" : heights[i],"in":i})
            
        res2=res2[::-1]
            
        print(len(res1),len(res2),len(heights))
        
        ans = 0
        
        for i,el in enumerate(heights):
            print(i)
            ans=max([(res2[i]-res1[i]-1)*el,ans])
            
            
        return ans
