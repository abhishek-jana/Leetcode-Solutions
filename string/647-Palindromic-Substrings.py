"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:

The input string length won't exceed 1000.
"""
# https://leetcode.com/problems/palindromic-substrings/discuss/392119/Solution-in-Python-3-(beats-~94)-(six-lines)-(With-Detaiiled-Explanation)
class Solution:
    def countSubstrings(self, s: str) -> int:
	    L, r = len(s), 0
	    for i in range(L):
	    	for a,b in [(i,i),(i,i+1)]:
	    		while a >= 0 and b < L and s[a] == s[b]: a -= 1; b += 1
	    		r += (b-a)//2
	    return r

# Alternate slower
class Solution:
    def countSubstrings(self, s: str) -> int:
	    def expand(left: int, right: int) -> int:
		    count = 0
		    while left >= 0 and right < len(s) and s[left] == s[right]:
			    # count the palindrome and expand outward
			    count += 1
			    left -= 1
			    right += 1
		    return count

	    palindromes = 0
	    for i in range(len(s)):
		    # the idea is to expand around the 'center' of the string, but the center could be 1 or 2 letters
			# e.g., babab and cbbd, hence the (i, i) and (i, i + 1)
		    palindromes += expand(i, i)
		    palindromes += expand(i, i+ 1)
	    return palindromes
