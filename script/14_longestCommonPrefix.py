#Longest Common Prefix:https://leetcode.com/problems/longest-common-prefix/description/
#Solution:
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        ans = ""
        if n == 0:
            return ans
        k = 0
        flag = True
        while flag:
            tmp = strs[0][0:k]
            for i in range(n):
                if strs[i][0:k] != tmp or k > len(strs[i]):
                    flag = False
                    break
            if flag:
                ans = tmp
                k += 1
        return ans