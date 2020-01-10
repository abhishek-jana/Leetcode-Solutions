'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
'''
# Time:  O(n * 2^n)
# Space: O(n * 2^n)
'''
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = [[]]
        for c in S:
            if c.isalpha():
                for i in range(len(result)):
                    result.append(result[i][:])
                    result[i].append(c.lower())
                    result[-1].append(c.upper())
            else:
                for s in result:
                    s.append(c)
        return map("".join, result)
'''
class Solution(object):
    def letterCasePermutation(self, S):
        out = ['']
        for ele in S:
            low = ele.lower()
            up = ele.upper() #this two variables are used to avoid repetitive use of .lower() and .upper()
            out = [x + low for x in out] + [x + up for x in out] if ele.isalpha() else [x + ele for x in out]
            print (out)
        return out

print (Solution().letterCasePermutation('aa34E'))
