#Valid Parentheses:https://leetcode.com/problems/valid-parentheses/description/
#Solution: StraightForward
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(':-3, ')':3, '{':-2, '}':2, '[':-1,']':1}
        b = []
        num = 0
        flag = True
        for w in s:
            if w in d:
                if d[w] < 0: # Left
                    b.append(w)
                    num += d[w]
                else:
                    if len(b) > 0 and d[w] + d[b[-1]] == 0 : #Pair
                        del b[-1]
                        num += d[w]
                    else:
                        flag = False
                        break
        if num != 0:
            flag = False
        return flag