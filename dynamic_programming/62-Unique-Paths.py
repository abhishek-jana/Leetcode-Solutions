'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[1]*m]*n
        #dp[0][0] = 1
        #dp[1][0] = 1
        #p[0][1] = 1
        for r in range(1, n):
            for c in range(1, m):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[n-1][m-1]

#print (Solution().uniquePaths(7,3))

#above solution is more intuitive but we can also reduce the space by O(n); where n is column size.
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        dp = [1]*n
        for i in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j-1] + dp[j]
        return dp[-1]

"""
m = 3
n = 3

1 1 1 1
1 2 3 4
1 3 6 10
"""

def uniquePaths( m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    if m == 0 or n == 0:
        return 0
    dp = [1]*n
    for i in range(1,m):
        for j in range(1,n):
            dp[j] = dp[j-1] + dp[j]
    return dp[-1]

print (uniquePaths(4,3))
