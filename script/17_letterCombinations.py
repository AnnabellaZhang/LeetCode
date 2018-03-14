# Letter Combinations of a Phone Number:https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Submission: DP
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        def dp(s):     
            ans = []
            dig = list(s)
            if len(dig) > 1:
                tmp = dp("".join(dig[1:]))
                l = list(d[dig[0]])
                for i in range(len(l)):
                    for j in range(len(tmp)):
                        ans.append(l[i] + tmp[j])
                return ans
            if len(dig) == 1:
                return list(d[dig[0]])
            if len(dig) == 0:
                return []
        return dp(digits)