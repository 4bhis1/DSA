#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        lis = []

        for string in strs:
            arr = [0]*26
            for i,el in enumerate(string):
                arr[ord(el)-97] = arr[ord(el)-97] +1
            
            if(tuple(arr) in hashmap):
                hashmap[tuple(arr)].append(string)
            else:
                hashmap[tuple(arr)] = []
                hashmap[tuple(arr)].append(string)
                # lis

        # print(hashmap)

        for i in hashmap:
            lis.append(hashmap[i])
            # print(hashmap[i])

        # print lis
        return lis
        


# @lc code=end

