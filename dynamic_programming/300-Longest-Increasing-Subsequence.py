'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n^2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''
class Solution:
    # Time O(n^2)
    # Space O(n)
    def lengthOfLIS(self,nums):
        max_count = 0
        LIS = []
        for i in range(len(nums)-1):
            LIS.append(nums[i])
            for j in range(i+1,len(nums)):
                if LIS[-1]<nums[j]:
                    LIS.append(nums[j])
            max_count = max(max_count,len(LIS))
            LIS = []
        return max_count
    # Using Dynamic Programming
    # Time O(n^2)
    # Space O(n)
    def lengthOfLIS2(self,nums):
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j] and dp[i]<dp[j]+1:
                    dp[i] = dp[j]+1
        max_length = 0
        for i in range(len(nums)):
            max_length = max(max_length,dp[i])
        return max_length

# lis returns length of the longest increasing subsequence 
# in arr of size n 
def lis(arr): 
    n = len(arr) 
  
    # Declare the list (array) for LIS and initialize LIS 
    # values for all indexes 
    lis = [1]*n 
  
    # Compute optimized LIS values in bottom up manner 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
  
    # Initialize maximum to 0 to get the maximum of all 
    # LIS 
    maximum = 0
  
    # Pick maximum of all LIS values 
    for i in range(n): 
        maximum = max(maximum , lis[i]) 
  
    return maximum 
# end of lis function 

def lengthOfLIS(nums):
        max_count = 0
        LIS = []
        for i in range(len(nums)-1):
            LIS.append(nums[i])
            for j in range(i+1,len(nums)):
                if LIS[-1]<nums[j]:
                    LIS.append(nums[j])
            max_count = max(max_count,len(LIS))
            LIS = []
        return max_count

array = [10,22,9,33,21,50,41,60,80]
import timeit
from timeit import Timer
t1 = Timer("lis([3,10,2,1,20])", "from __main__ import lis")
print (t1.timeit(number=100000),"milliseconds")
t2 = Timer("lengthOfLIS([3,10,2,1,20])", "from __main__ import lengthOfLIS")
print (t2.timeit(number=100000),"milliseconds")

#print (Solution().lengthOfLIS2([3,10,2,1,20] ))

# Binary Search

def lengthOfLIS(self, nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) / 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size
# Taken from https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
