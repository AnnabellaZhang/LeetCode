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

# Solution
