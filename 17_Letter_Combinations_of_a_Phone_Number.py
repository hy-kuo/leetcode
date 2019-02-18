class Solution:
    digit2alpha = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']
                      }
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        if len(digits)==1:
            return self.digit2alpha[digits]
        elif not len(digits):
            return []
        else:
            last_digit = digits[-1]
            pre = self.letterCombinations(digits[0:-1])
            combination = []
            for com in pre:
                for ch in self.digit2alpha[last_digit]:
                    new_comb = com+ch
                    combination.append(new_comb)
            return combination
            
            