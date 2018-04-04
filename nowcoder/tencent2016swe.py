#1
# -*- coding:utf-8 -*-

class GrayCode:
    def getGray(self, n):
        # write code here
        if n == 1:
            return ["0","1"]
        l1 = self.getGray(n-1)
        l1 += l1[::-1]
        l2 = []
        for i in range(len(l1)):
            l2.append(l1[i][0])
        for i in range(2**(n-2)):
            l2.insert(0,l2.pop(-1))
        ans = []
        for i in range(len(l1)):
            ans.append(l2[i]+l1[i])
        return ans


#2
# -*- coding:utf-8 -*-
 
class Gift:
    def getValue(self, gifts, n):
        # write code here
        if n == 1:
            return gifts[0]
        if n == 0:
            return 0
        gifts.sort()
        mid = n//2
        if gifts[mid] == gifts[0] or (gifts[mid-1] == gifts[mid+1]):
            return gifts[mid]
        else:
            return 0