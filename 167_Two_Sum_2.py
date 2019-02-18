class Solution:
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        table = {}
        for i, n in enumerate(numbers):

            if target-n in table:
                table[target-n].append(i+1)
            else:
                table[target-n] = [i+1]
        
        for n in table:
            if target-n in table:
                if target-n != n:
                    return [table[n][0], table[target-n][0]]
                else:
                    return [table[n][0], table[n][1]]