#Container With Most Water:https://leetcode.com/problems/container-with-most-water/description/
#Solution:
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        b,e = 0,len(height)-1
        ans = -1
        while e-b > 0:
            tmp = min(height[e],height[b])*(e-b)
            if tmp > ans:
                ans = tmp
            if height[e] < height[b]:
                e -= 1
            else:
                b += 1
        return ans 

#Bad: Time Limit Exceeded
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = -1
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                if min(height[i],height[j])*(j-i) > ans:
                    ans = min(height[i],height[j])*(j-i)
        return ans