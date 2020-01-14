"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

# Time O(n)
# Space O(1)
# https://leetcode.com/problems/valid-anagram/solution/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counter = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1

        for char in t:
            if char in counter:
                counter[char] -= 1
            else:
                return False

        for val in counter.values():
            if val != 0:
                return False

        return True
