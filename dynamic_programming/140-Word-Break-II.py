'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''


class Solution(object):
    # https://discuss.leetcode.com/topic/12997/11ms-c-solution-concise
    def __init__(self):
        self.solution = {}

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        try:
            return self.solution[s]
        except KeyError:
            pass
        result = []
        if s in wordDict:
            result.append(s)
        for i in range(1, len(s)):
            word = s[i:]
            if word in wordDict:
                rem = s[:i]
                prev = self.wordBreak(rem, wordDict)
                result.extend([res + ' ' + word for res in prev])
        self.solution[s] = result
        return result

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.result = []
        self.dfs(s, wordDict, '')
        return self.result

    def dfs(self, s, wordDict, currStr):
    	if self.check(s, wordDict):
    		if len(s) == 0:
    			self.result.append(currStr[1:])
    		for i in range(1, len(s)+1):
    			if s[:i] in wordDict:
    				self.dfs(s[i:], wordDict, currStr + ' ' + s[:i])

    def check(self, s, wordDict):
    	dp = [False for _ in range(len(s)+1)]
    	dp[0] = True

    	for i in range(len(s)):
    		for j in range(i, -1, -1):
    			if dp[j] and s[j:i+1] in wordDict:
    				dp[i+1] = True
    				break

    	return dp[len(s)]
