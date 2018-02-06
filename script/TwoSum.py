# Two Sum: https://leetcode.com/problems/two-sum/description/
#Submission: Bubble Sort + bidirectional search -> Depend on sort
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return []
        else:
            def bubble_sort(arr,index):
                n = len(arr)
                k = n
                for i in range(n):
                    flag = 1
                    for j in range(1,k):
                        if arr[j-1] > arr[j]:
                            arr[j-1],arr[j] = arr[j],arr[j-1]
                            index[j-1],index[j] = index[j],index[j-1]
                            k = j
                            flag = 0
                    if flag:
                        break
                return arr,index
            index = list(range(len(nums)))
            nums,index = bubble_sort(nums,index)
            low = 0
            high = len(nums)-1
            while True:
                if nums[low]+nums[high] < target:
                    low = low+1
                elif nums[low]+nums[high] > target:
                    high = high-1
                else:
                    return [index[low],index[high]]

# 1 use directory to save time with space -> O(n)?
# 2 nums may have same number
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return []
        else:
            for i in range(len(nums)):
                if i == 0:
                    dic = {nums[i]:i,target-nums[i]:i}
                else:
                    if nums[i] in dic:
                        if nums[i] + nums[dic[nums[i]]] == target:
                            return [dic[nums[i]],i]
                    else:
                        dic[nums[i]] = i
                        dic[target-nums[i]] = i