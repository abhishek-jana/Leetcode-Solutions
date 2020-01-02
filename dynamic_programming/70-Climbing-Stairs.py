'''

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''

class Solution:
    def climbStairs(self,n):
        if n == 1 or n == 2:
            return n
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)
    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
        	return 0

        dp = [0]*n
        dp[0], dp[1] = 1, 2

        for index in range(2, n):
        	dp[index] = dp[index-1] + dp[index-2]
        return dp[n-1]

# Time: O(N)
# Space: O(N)

print (Solution().climbStairs(7))

#Time complexity : O(n). Single loop upto n.

#Space complexity : O(n). array of size n is used.
