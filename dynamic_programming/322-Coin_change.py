'''

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1

'''

class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                #print (dp[x],dp[x-coin]+1,x,coin)
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
        #return dp
'''
Time complexity : O(S*n). On each step the algorithm finds the next F(i) in n iterations, where 1 ≤ i ≤ S. Therefore in total the iterations are S*n.
Space complexity : O(S). We use extra space for the memoization table.
'''

print (Solution().coinChange([6,7,21,25],63))

class Solution2():
    def coinChange2(self, coins, amount):
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                #print (dp[x],dp[x-coin]+1,x,coin)
                dp[x] += dp[x - coin]
        return dp[amount] #if dp[amount] != float('inf') else -1
        #return dp

# Driver program to test above function 
arr = [1, 2, 3] 
m = len(arr) 
n = 4

print (Solution2().coinChange2(arr,n)) 

