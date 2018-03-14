#Palindrome Number:https://leetcode.com/problems/palindrome-number/description/
#Solution:
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]
#Complicated:
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        if s[0] == "+" or s[0] == "-":
            return False
        if len(s) == 0:
            return False
        if len(s) == 1:
            return True
        b,e = 0,len(s)-1
        while e-b >= 0:
            if s[e] != s[b]:
                return False
            e -= 1
            b += 1
        return True