#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store = {}

        for i,el in enumerate(nums):
            if(el in store):
                return [store[el]["index"],i]
            else:
                store[target-el]={"index" : i}

            # print(store)
# @lc code=end

