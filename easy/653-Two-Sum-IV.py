'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''
# http://yueguo1217.com/leetcode-653-two-sum-iv-input-is-a-bst-easy-76-in-python/


# Fastest

class Solution:
    def __init__(self):
        self.theSet = set()
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is not None:
            if k - root.val in self.theSet:
                return True
            else:
                self.theSet.add(root.val)
                return self.findTarget(root.left, k) or self.findTarget(root.right, k)
        return False
        
