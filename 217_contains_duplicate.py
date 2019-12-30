'''

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

'''
# Time complexity : O(n). We do search() and insert() for n times and each operation taikes constant time.

#Space complexity : O(n). The space used by a hash table is linear with the number of elements in it.


class Solution:
    def containsDuplicate(self,nums):
        temp = {}
        for i in nums:
            if i in temp:
                return True
            else:
                temp[i] = None
        return False
'''
# Time:  O(n)
# Space: O(n)

class Solution(object):
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))
'''
duplicate = Solution()

print (duplicate.containsDuplicate([1,1,1,3,3,4,3,2,4,2]*1000000))
