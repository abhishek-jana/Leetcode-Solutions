'''
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.


Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
'''


class Solution:
    def combinationSum4(self,nums,target):
        length = target + 1
        dp = [0]*length
        dp[0] = 1
        nums.sort()
        for i in range(1,length):
            for j in range(len(nums)):
                if nums[j] <= i:
                    dp[i] = dp[i] + dp[i-nums[j]]
                else:
                    break
        return dp[target]

print (Solution().combinationSum4([1,2,3],4))

# Time:  O( n * t), t is the value of target.
# Space: O(t)
