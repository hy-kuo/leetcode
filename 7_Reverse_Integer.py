class Solution:
    def reverse(self, x: 'int') -> 'int':
        x_s = str(x)
        ans = 1
        if x_s[0] == '-':
            ans *= -1
            x_s = x_s[1::]
        x_s = x_s[::-1]
        ans *= int(x_s)
        if ans > 2**31-1 or ans < -(2**31):
            ans = 0
        return ans