"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.


Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        begin, end, res, mostFrequentCounter = 0, 0, 0, 0
        map = {}
        while end < len(s):
            char = s[end]
            map[char] = map.get(char, 0) + 1
            if mostFrequentCounter < map[char]:
                mostFrequentCounter = map[char]
            end += 1

            while (end-begin > mostFrequentCounter+k):
                char = s[begin]
                map[char] -= 1
                mostFrequentCounter = max(map.values())
                begin += 1

            res = max(end-begin, res)

        return res
