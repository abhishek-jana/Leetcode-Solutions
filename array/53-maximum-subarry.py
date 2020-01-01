'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''
# Time:  O(n)
# Space: O(1)

class Solution:
    def maxsubArray(self,nums):
        current = float('-inf')
        result = float('-inf')
        for i in nums:
            current = max(current+i,i)
            result = max(current,result)
        return result

array = Solution()
print (array.maxsubArray([-2,1,-3,4,-1,2,1,-5,4]))

# Using Divide and Conquer

# Python3 implementation of the approach 

class Node: 
	
	def __init__(self, x): 
		
		# To store the maximum sum for a sub-array 
		self._max = x 
		
		# To store the maximum prefix sum for a sub-array 
		self._pre = x 
		
		# To store the maximum suffix sum for a sub-array 
		self._suf = x 
		
		# To store the total sum for a sub-array 
		self._sum = x 
		
# Function to merge the 2 nodes left and right 
def merg(l, r): 
	
	# Creating node ans 
	ans = Node(0) 

	# The max prefix sum of ans Node is maximum of 
	# a) max prefix sum of left Node 
	# b) sum of left Node + max prefix sum of right Node 
	# c) sum of left Node + sum of right Node 
	ans._pre = max(l._pre, l._sum+r._pre, l._sum+r._sum) 

	# The max suffix sum of ans Node is maximum of 
	# a) max suffix sum of right Node 
	# b) sum of right Node + max suffix sum of left Node 
	# c) sum of left Node + sum of right Node 
	ans._suf = max(r._suf, r._sum+l._suf, l._sum+r._sum) 
	
	# Total sum of ans Node = total sum of 
	# left Node + total sum of right Node 
	ans._sum = l._sum + r._sum 
	
	# The max sum of ans Node stores the answer 
	# which is the maximum value among: 
	# prefix sum of ans Node 
	# suffix sum of ans Node 
	# maximum value of left Node 
	# maximum value of right Node 
	# prefix value of left Node + suffix value of right Node 
	ans._max = max(ans._pre, ans._suf, ans._sum, 
					l._max, r._max, l._suf+r._pre) 

	# Return the ans Node 
	return ans 

# Function for calculating the 
# max_sum_subArray using divide and conquer 
def getMaxSumSubArray(l, r, ar): 

	if l == r: return Node(ar[l]) 

	mid = (l + r) // 2
	
	# Call method to return left Node: 
	left = getMaxSumSubArray(l, mid, ar) 
	
	# Call method to return right Node: 
	right = getMaxSumSubArray(mid+1, r, ar) 
	
	# Return the merged Node: 
	return merg(left, right) 

# Driver code 
if __name__ == "__main__": 

	ar = [-2, -5, 6, -2, -3, 1, 5, -6] 
	n = len(ar) 
	ans = getMaxSumSubArray(0, n-1, ar) 
	print("Answer is", ans._max) 

'''
Time Complexity: The getMaxSumSubArray() recursive function generates the following recurrence relation.
T(n) = 2 * T(n / 2) + O(1) note that conquer part takes only O(1) time. So on solving this recurrence using Master’s Theorem we get the time complexity of O(n).
'''


# Alternate sol

# A Divide and Conquer based program
# for maximum subarray sum problem

# Find the maximum possible sum in
# arr[] auch that arr[m] is part of it
def maxCrossingSum(arr, l, m, h) :

	# Include elements on left of mid.
	sm = 0; left_sum = -10000

	for i in range(m, l-1, -1) :
		sm = sm + arr[i]

		if (sm > left_sum) :
			left_sum = sm


	# Include elements on right of mid
	sm = 0; right_sum = -1000
	for i in range(m + 1, h + 1) :
		sm = sm + arr[i]

		if (sm > right_sum) :
			right_sum = sm


	# Return sum of elements on left and right of mid
	return left_sum + right_sum;


# Returns sum of maxium sum subarray in aa[l..h]
def maxSubArraySum(arr, l, h) :

	# Base Case: Only one element
	if (l == h) :
		return arr[l]

	# Find middle point
	m = (l + h) // 2

	# Return maximum of following three possible cases
	# a) Maximum subarray sum in left half
	# b) Maximum subarray sum in right half
	# c) Maximum subarray sum such that the
	#	 subarray crosses the midpoint
	return max(maxSubArraySum(arr, l, m),
			maxSubArraySum(arr, m+1, h),
			maxCrossingSum(arr, l, m, h))


# Driver Code
arr = [2, 3, 4, 5, 7]
n = len(arr)

max_sum = maxSubArraySum(arr, 0, n-1)
print("Maximum contiguous sum is ", max_sum)

'''
Time Complexity: maxSubArraySum() is a recursive method and time complexity can be expressed as following recurrence relation.
T(n) = 2T(n/2) + Θ(n)
The above recurrence is similar to Merge Sort and can be solved either using Recurrence Tree method or Master method. 
It falls in case II of Master Method and solution of the recurrence is Θ(nLogn).
'''

    
