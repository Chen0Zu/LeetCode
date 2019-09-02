'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        n = len(nums)
        for i in range(n):
                if nums[i] != val:
                        if i > j:
                                nums[j] = nums[i]
                        i += 1
                        j += 1
                else:
                        i += 1

        return j

nums = [3,2,2,3]
print(Solution().removeElement(nums, 3))