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
        # for each num I will check whether num-1 exists
        # if yes, then I ignore this num
        # Otherwise if num-1 doesn't exist, then I will go till I can find num+1
        # so in a way I am only checking each number max once and once in set.

        st = set(nums)
        mx = 0
        for num in nums:
            if num-1 not in st:
                tmp = 1
                while num+1 in st:
                    tmp += 1
                    num += 1
                mx = max(mx, tmp)

        return mx
'''
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print (i)
'''
