class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        table = {}
        n = len(s)
        if n:
            max_lps = s[0]
        else:
            max_lps = ""
        for i in range(n):
            table[(i,i)] = True
            if i < n-1:
                table[(i,i+1)] = True if s[i] == s[i+1] else False
                if table[(i,i+1)]:
                    max_lps = s[i:i+2]
                    
        for i in reversed(range(n)):
            for j in range(i+2, n):
                if i+1<n and j-1>=0:
                    
                    table[(i, j)] = table[(i+1,j-1)] if s[i] == s[j] else False
                    if table[(i, j)] and j-i+1 > len(max_lps):
                        max_lps =s[i:j+1]
        return max_lps
                
            