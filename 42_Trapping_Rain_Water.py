class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        left_up_max = 0
        left_max = {}
        right_up_max = 0
        right_max = {}
        
        for i,val in enumerate(height):
            if val > left_up_max:
                left_max[i] = val
                left_up_max = val
            else:
                left_max[i] = left_up_max
        for i, val in reversed(list(enumerate(height))):
            if val > right_up_max:
                right_max[i] = val
                right_up_max = val
            else:
                right_max[i] = right_up_max
        ans = 0
        for i, val in enumerate(height):
            ans += min(left_max[i], right_max[i]) - val
        return ans
   
        