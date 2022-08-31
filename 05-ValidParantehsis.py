# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        
        arr = []
        
        for j in s :
            
            if(len(arr) == 0 or j == '{' or j =='[' or j == '(' ):
                arr.append(j)
            elif((arr[-1] == '[' and j==']') or (arr[-1] == '{' and j=='}') or (arr[-1] == '(' and j==')')):
                arr.pop()
            else:
                arr.append(j)
            
            
            # print(arr)
        
        if(len(arr) == 0):
            return True
        else:
            return False
        
        