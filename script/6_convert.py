#ZigZag Conversion:https://leetcode.com/problems/zigzag-conversion/
#Solution:
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0 or numRows > len(s) or numRows == 1:
            return s
        index,step = 0,1
        L = ['']*numRows
        for x in s:
            if index == 0:
                step = 1
            if index == numRows-1:
                step = -1
            L[index] += x
            index += step
        return ''.join(L)