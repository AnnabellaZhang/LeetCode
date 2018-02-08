#Median of Two Sorted Arrays: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#Submission: traversing -> O(max(m,n))
class Solution:
    def findMedianSortedArrays(self,nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        flag = False
        if (m + n) % 2 == 0:
            flag = True
        if len(nums1) == 0 or len(nums2) == 0:
            if len(nums1) == 0 and len(nums2) == 0:
                return 0
            elif len(nums1) == 0:
                if flag:
                    return (nums2[int(n / 2)-1] + nums2[int(n / 2)])/2
                else:
                    return nums2[int(n / 2)]
            else:
                if flag:
                    return (nums1[int(m / 2)-1] + nums1[int(m / 2)])/2
                else:
                    return nums1[int(m / 2)]
        s1_p, s2_p = 0, 0
        tmp = 0
        mi,ma = -1,-1
        while tmp < (m + n) / 2:
            tmp = tmp + 1
            if s2_p >=n:
                mi = nums1[s1_p]
                s1_p = s1_p + 1
            elif s1_p >= m:
                mi = nums2[s2_p]
                s2_p = s2_p + 1
            elif nums1[s1_p] < nums2[s2_p]:
                mi = nums1[s1_p]
                s1_p = s1_p+1
            else:
                mi = nums2[s2_p]
                s2_p = s2_p+1
        if flag == False:
            return mi
        else:
            if s1_p < m and s2_p < n:
                ma = min(nums1[s1_p], nums2[s2_p])
            elif s1_p >= m:
                ma = nums2[s2_p]
            else:
                ma = nums1[s1_p]
            return (mi + ma) / 2

# Solution : From the middle of each List
class Solution:
    def findMedianSortedArrays(self,nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if n < m:
            nums1,nums2,m,n = nums2,nums1,n,m
        i = int(m/2)
        j = int((m+n)/2-i)
        flag = ( (m+n) % 2 == 0) #need to /2
        while True:
            if (j==0 or i==m or nums2[j-1] <= nums1[i]) and (i==0 or j==n or nums1[i-1] <= nums2[j]):
                break
            elif i<m and j>0 and nums2[j-1]>nums1[i]:
                i = i+1
                j = int((m+n)/2-i)
            elif i>0 and j<n and nums1[i-1]>nums2[j]:
                i = i-1
                j = int((m+n)/2-i)
        if flag:
            if i>0 and j>0:
                mi = max(nums1[i-1],nums2[j-1])
            elif i==0:
                mi = nums2[j-1]
            else:
                mi = nums1[i-1]
            if i<m and j<n:
                ma = min(nums1[i],nums2[j])
            elif i==m:
                ma = nums2[j]
            else:
                ma = nums1[i]
            return (mi+ma)/2
        else:
            if i == m:
                return nums2[j]
            if j == n:
                return nums1[i]
            return min(nums1[i],nums2[j])
                    