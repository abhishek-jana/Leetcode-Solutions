'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''

class Solution(object):
    # Actually we can make this solution more general
    def validPalindrome(self, s):
        return self.validPalindromeHelper(s, 0, len(s) - 1, 1)

    def validPalindromeHelper(self, s, left, right, budget):
        #print (budget)
        # Note that budget can be more than 1
        while left < len(s) and right >= 0 and left <= right and s[left] == s[right]:
            left += 1
            right -= 1
        if left >= len(s) or right < 0 or left >= right:
            return True
        if budget == 0:
            return False
        budget -= 1
        return self.validPalindromeHelper(s, left + 1, right, budget) or \
    self.validPalindromeHelper(s, left, right - 1, budget)

print (Solution().validPalindrome('acacba'))

# if only one letter is there
# Time O(n)
# Space O(1)
class Solution:
    def validPalindrome(self,s):
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left, right-1) or self.isPalindrome(s, left+1, right)
            left, right = left+1, right-1
        return True

    def isPalindrome(self,s,left,right):
        while left < right:
            if s[left] != s[right]:
                return False
            left,right = left + 1, right - 1
        return True

print (Solution().validPalindrome('aba'))
