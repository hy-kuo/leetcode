class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        table = {}
        for idx, n in enumerate(nums):
            if target-n not in table:
                table[target-n] = [idx]
            else:
                table[target-n].append(idx)
        for key in table:
            if target-key in table: 
                if key == target-key and len(table[key])>1:
                    return [table[key][0],table[key][1]]
                elif key != target-key:
                    return [table[key][0], table[target-key][0]]