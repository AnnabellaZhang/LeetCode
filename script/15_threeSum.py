#3Sum:https://leetcode.com/problems/3sum/description/
#Solution: Transfer to 2Sum
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def twoSum(nums,c):
            #nums有序
            b,e = 0,len(nums)-1
            ans = []
            while e-b>0:
                #print("e = {},b = {}".format(e,b))
                if nums[e]+ nums[b] > c:
                    e -=1
                elif nums[e]+ nums[b] < c:
                    b += 1
                else:
                    if len(ans) == 0 or [nums[b],nums[e]] != ans[-1]:
                        ans.append([nums[b],nums[e]])
                    e -= 1
                    b += 1   
            return ans
        nums.sort()
        #print(nums)
        ans = []
        c = 1
        for i in range(len(nums)-2):
            #tmp[i],tmp[0] = tmp[0],tmp[i]
            if nums[i] == c:
                i += 1
                continue
            c = nums[i]
            tsm = twoSum(nums[i+1:],-nums[i])
            #print("tmp[0] = {},tsm = {}".format(nums[i],tsm))
            if len(tsm) > 0:
                for j in range(len(tsm)):
                    ans.append([nums[i]] + tsm[j])
        return ans