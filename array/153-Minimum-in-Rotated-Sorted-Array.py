'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

'''



class Solution:
    def __init__(self,nums):
        self.nums = nums
        #self._left = 0
        #self._right = len(self.nums)-1
    def isSmaller(self,_left,_right):
        if self.nums[_left] < self.nums[_right]:
            return True
        else:
            return False
    def findMin(self):
        _left = 0
        _right = len(self.nums)-1
        if self.isSmaller(_left,_right):
            return self.nums[0]
        else:
            while _right >= _left:
                mid = _left + (_left + _right)//2
                # if the mid element is greater than its next element then mid+1 element is the smallest
                # This point would be the point of change. From higher to lower value.
                if self.isSmaller(mid+1,mid):
                    return self.nums[mid+1]
                # if the mid element is lesser than its previous element then mid element is the smallest
                if self.isSmaller(mid,mid-1):
                    return mid
                # if the mid elements value is greater than the 0th element this means
                # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
                if self.isSmaller(0,mid):
                    _left = mid + 1
                # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
                else:
                    _right = mid-1

array = Solution([4,5,1,2,3])

print (array.findMin())


'''
Time Complexity : Same as Binary Search O(logN)
Space Complexity : O(1)

'''

