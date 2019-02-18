class Solution:
    def isValid(self, s: 'str') -> 'bool':
        stack = []
        if not len(s):
            return True
        for x in s:
            if not len(stack):
                stack.append(x)
            else:
                y = stack.pop(-1)
                if x == ')' and y == '(':
                    pass
                elif x =='}' and y =='{':
                    pass
                elif x ==']' and y=='[':
                    pass
                else:
                    stack.append(y)
                    stack.append(x)
        if len(stack):
            return False
        else:
            return True
            