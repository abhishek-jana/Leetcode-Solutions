'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''
'''
Start from idx = len(nums)-2
Set target = len(nums)-1, which is the last index.
If current idx + num[idx] >= target, then starting from idx and destination is reachable.
From other positions, if we can reanch current idx then destination is also reachable.
So update the target = idx.
Time: O(n)
Space: O(1)
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return True

        target = len(nums) - 1
        for idx in range(target-1,-1,-1): # iterate from the second last index to 0.
            if idx + nums[idx] >= target:
                target = idx

        return target == 0
