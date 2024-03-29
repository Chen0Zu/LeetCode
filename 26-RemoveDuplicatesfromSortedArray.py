'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        j = 1
        while j < n:
                if nums[i] == nums[j]:
                        j = j+1
                else:
                        nums[i+1] = nums[j]
                        i = i+1
                        j = j+1
        return i+1

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))