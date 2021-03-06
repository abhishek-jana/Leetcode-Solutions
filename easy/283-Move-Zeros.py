'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pos = 0
        for i in range(n):
            if nums[i] != 0:
                temp = nums[pos]
                nums[pos] = nums[i]
                nums[i] = temp
                pos += 1


# O(n)
num = [0, 0, 1, 0, 3, 12]
Solution().moveZeroes(num)
print(num)
