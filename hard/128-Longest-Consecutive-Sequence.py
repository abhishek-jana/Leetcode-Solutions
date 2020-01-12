"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        res = 0
        while nums:
            stack = [next(iter(nums))]
            tmp = 0
            while stack:
                tmp += 1
                curr = stack.pop()
                nums.discard(curr)
                if curr + 1 in nums: stack.append(curr + 1)
                if curr - 1 in nums: stack.append(curr - 1)
            res = max(res, tmp)
        return res
'''
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print (i)
'''
