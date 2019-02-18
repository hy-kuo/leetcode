class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        key = S.replace('-', '')
        key = key.upper()
        ans = ''
        i = 0
        if len(key)%K == 0:
            ans += key[0:K]
            i = K
        else:
            ans += key[0:(len(key)%K)]
            i = len(key)%K
        while(i<len(key)):
            ans += '-'
            ans += key[i:i+K]
            i += K
        return ans
            
        