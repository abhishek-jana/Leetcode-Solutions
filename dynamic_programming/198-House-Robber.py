'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

'''
######################################
'''
dp[i] = max (hval[i] + dp[i-2], dp[i-1])

hval[i] + dp[i-2] is the case when thief
decided to rob house i. In that situation 
maximum value will be the current value of
house + maximum value stolen till last 
robbery at house not adjacent to house 
i which will be house i-2.  
 
dp[i-1] is the case when thief decided not 
to rob house i. So he will check adjacent 
house for maximum value stolen till now. 
'''
class Solution:
    #Time complexity = O(n)
    #Space complexity = O(n)
    def rob(self,nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        dp = [0]*len(nums)
        dp[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        return dp[-1]
    #We can optimize extra space, by using two variables to store value dp[i-1] and dp[i-2].
    #Time O(n)
    #Space O(n) 
    def rob2(self,nums):
        val1 = nums[0]
        val2 = nums[1]
        if len(nums) == 0: 
            return 0       
        if len(nums) == 1:  
            return val1                
        if len(nums) == 2:
            return max(val1,val2)
        
        max_val = 0
              
        for i in range(2,len(nums)):
            max_val = max(nums[i]+val1,val2])
            val1 = val2
            val2 = max_val
        return dp[-1]

# Driver to test above code  
def main(): 
  
    # Value of houses 
    hval = [6, 7, 1, 3, 8, 2, 4] 
  
    print("Maximum loot value : {}". 
        format(Solution().rob(hval))) 
  
if __name__ == '__main__': 
    main() 

