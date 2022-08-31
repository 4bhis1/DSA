# https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/


class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        
        stck = []
        res = []
        
        for i in range(n-1,-1,-1):
            
            while(len(stck) !=0 and stck[-1]<arr[i]):
                stck.pop()
            
            if(len(stck) == 0):
                res.append(-1)
            elif(arr[i]<stck[-1]):
                res.append(stck[-1])
            
            stck.append(arr[i])
            
        # print(res)
        
        return res[::-1]
            
