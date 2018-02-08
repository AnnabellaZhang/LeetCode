# Reverse Integer:https://leetcode.com/problems/reverse-integer/description/
# Submission: Straightforward
class Solution:
    def reverse(self,x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        import math as m
        flag = (x < 0)
        x = abs(x)
        num = ""
        r = "8463847421"
        bit = int(m.log(x, 10))
        n = bit
        tmp = x
        for i in range(n+1):
            num = num+str(int(tmp / m.pow(10, bit)))
            tmp = tmp % m.pow(10, bit)
            bit = bit - 1
        ans = int(num[::-1])
        if int(ans) >= 2147483647:
            return 0
        if flag:
            ans = ans * (-1)
        return ans

# Solution: use string
class Solution:
    def reverse(self,x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        flag = (x<0)
        ans = int(str(abs(x))[::-1])
        if ans >= 2**31-1:
            return 0
        if flag:
            ans = ans * (-1)
        return ans