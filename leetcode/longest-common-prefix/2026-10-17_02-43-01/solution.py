class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=""
        for i in range(len(strs[0])):
            for words in strs[1:]:
                if i>=len(words) or words[i]!=strs[0][i]:
                    return prefix
            prefix+=strs[0][i]
        return prefix
                
        