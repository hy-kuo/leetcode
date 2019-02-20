from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        c = Counter()
        if len(s) < 2:
            return  len(s)
        max_lgh = 0
        i = 0
        
        for j in range(0, len(s)):
            while s[j] in c:
                #print(c, s[i])
                del c[s[i]]
                i += 1
            c[s[j]] = 1
            max_lgh = max(max_lgh, j-i+1)
        return max_lgh