'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def ThreeSum(self,nums):
        nums.sort()
        if len(nums)>=3 and nums[0]==nums[len(nums)-1] and nums[0] == 0:
            return [[0,0,0]]
        result = []
        for i in range(len(nums)-1):
            right = i + 1
            end = len(nums)-1
            while right < end:
                total =  (nums[i]+nums[right]+nums[end])
                if total == 0:
                    result.append([nums[i],nums[right],nums[end]])
                    right += 1
                    end -= 1
                elif total < 0:
                    right += 1
                else:
                    end -= 1
        #we can't take set of list, so we convert to tuple
        result = set([tuple(t) for t in result])
        return [list(t) for t in result]

#Space = O(1)
#Time = O(n^2)

res = Solution()
print (res.ThreeSum([-1,0,1,2,-1,-4]))
