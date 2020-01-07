'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''


class Solution:
    def merge(self,num1,m,num2,n):
        last,i,j = m+n-1,m-1,n-1
        while i > 0 and j > 0:
            if num1[i] > num2[j]:
                num1[last] = num1[i]
                last,i = last - 1, i - 1
            else:
                num1[last] = num2[j]
                last, j = last - 1, j - 1
        while j > 0:
            num1[last] = num2[j]
            last, j = last - 1, j - 1
            
print (Solution().merge([1,2,3,0,0,0],3,[2,5,6],3))
            
