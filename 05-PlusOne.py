# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        
        for i in range(len(digits)-1,-1,-1):
            if (carry == 1):
                
                if (digits[i]+carry > 9):
                    digits[i] = 0
                    carry = 1
                else:
                    digits[i]=digits[i]+1
                    carry = 0
            else: 
                carry = 0
                break
        else:
            if(carry == 1):
                digits.insert(0,1)
            
        return digits
            