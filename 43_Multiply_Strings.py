class Solution:
    def multiply(self, num1: 'str', num2: 'str') -> 'str':
        num1 = [int(x) for x in list(num1)[::-1]]
        num2 = [int(x) for x in list(num2)[::-1]]
        ans = [0] * (len(num1) + len(num2))
        for idx_1, x in enumerate(num1):
            carry = 0
            for idx_2, y in enumerate(num2):
                ans[idx_1+idx_2] += x*y
        
        #handle carry
        carry = 0
        for i, val in enumerate(ans):
            ans[i], carry = (val + carry)%10, int((val + carry)/10)            
        
        i = 0
        for i in reversed(range(len(ans))):
            if ans[i]!=0:
                break
        return ''.join(str(e) for e in ans[i::-1])
        
                