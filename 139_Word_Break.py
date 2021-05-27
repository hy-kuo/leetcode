class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        flag = False
        for w in wordDict:
            if s == w:
                return True
            if w in s:
                s_list = list(filter(None, s.split(w)))
                flag = True
                for subs in s_list:
                    flag = flag and self.wordBreak(subs, wordDict)
                if flag == True:
                    return flag
        return flag

        
        
