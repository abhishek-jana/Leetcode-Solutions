'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''
class Solution:
    def isPalindrome(self, s):
    # @param s, a string
    # @return a boolean
        def isPalindrome(self, s):
            if len(s) < 2:          
                return True
            head, tail = 0, len(s)-1
            while head < tail:
                if not s[head].isalnum():
                    head += 1
                elif not s[tail].isalnum():
                    tail -= 1
                else:
                    if s[head].lower() == s[tail].lower():
                        head += 1
                        tail -= 1
                    else:
                        return False
            return True
        
    # Time O(n)
    # Space O(1)
