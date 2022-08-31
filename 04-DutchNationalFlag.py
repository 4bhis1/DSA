# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, arr: List[int]) -> None:
        
        s =0
        m=0
        e=len(arr)-1
        
        while(e>=m):
            if(arr[m] == 0):
                arr[s],arr[m] = arr[m],arr[s]
                s=s+1
                m=m+1
            elif(arr[m]==1):
                m=m+1
            else:
                arr[e],arr[m]=arr[m],arr[e]
                e=e-1
                