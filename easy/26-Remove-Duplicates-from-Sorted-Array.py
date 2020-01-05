'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''

class Solution:
    def removeDuplicates(self,nums):
        nums = set(nums)
        return len(nums)
    def removeDuplicates2(self,arr):
        n = len(arr)
        if n == 0 or n == 1: 
            return n 
    
        # To store index of next 
        # unique element 
        j = 0
    
        # Doing same as done 
        # in Method 1 Just 
        # maintaining another  
        # updated index i.e. j 
        for i in range(0, n-1): 
            if arr[i] != arr[i+1]: 
                arr[j] = arr[i] 
                j += 1
    
        arr[j] = arr[n-1] 
        j += 1
        return j
    def removeDuplicates3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        index_i = 0

        for index_j in range(1, len(nums)):
            if nums[index_i] != nums[index_j]:
                index_i += 1
                nums[index_i] = nums[index_j]

        return index_i + 1
    
print (Solution().removeDuplicates3([0,0,1,1,1,2,2,3,3,4]))

# Time O(n)
# Space O(1)

# To return the array
# This function returns new  
# size of modified array 
def removeDuplicates(arr, n): 
    if n == 0 or n == 1: 
        return n 
  
    # To store index of next 
    # unique element 
    j = 0
  
    # Doing same as done 
    # in Method 1 Just 
    # maintaining another  
    # updated index i.e. j 
    for i in range(0, n-1): 
        if arr[i] != arr[i+1]: 
            arr[j] = arr[i] 
            j += 1
  
    arr[j] = arr[n-1] 
    j += 1
    return j 
  
# Driver code 
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5] 
n = len(arr) 
  
# removeDuplicates() returns 
# new size of array. 
n = removeDuplicates(arr, n) 
  
# Print updated array 
for i in range(0, n): 
    print (" %d "%(arr[i]))
