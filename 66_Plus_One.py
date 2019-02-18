class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        digits = digits[::-1]
        carry = 1
        
        for idx in range(0, len(digits)):
            digits[idx], carry = (digits[idx]+carry)%10, int((digits[idx]+carry)/10)
            if carry == 0:
                break
        if carry == 1:
            digits.append(carry)
            
        return digits[::-1]