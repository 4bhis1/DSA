class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    
        a=0
        b=0
        
        for i in range(len(nums1)-1,m-1,-1):
            if(not nums1[i]):
                nums1.pop()
            else :
                break
            
        print(nums1)
        
        while (1) :
            if(a == len(nums1) or b == len(nums2)):
                break
            
            
            if(nums1[a]>nums2[b]) :
                nums1.insert(a,nums2[b])
                b=b+1
            elif (nums1[a]<=nums2[b]):
                a=a+1
            
            # print(nums1,nums2)
            
        if(b<len(nums2)):
            for i in range(b,len(nums2)):
                nums1.append(nums2[i])
                # print(nums1)
        