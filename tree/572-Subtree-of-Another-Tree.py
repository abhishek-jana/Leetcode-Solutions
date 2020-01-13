'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s, t):
        if t is None:
            return True
        if s is None:
            return False
        if self.equals(s,t):
            return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def equals(self,x,y):
        if x is None and y is None:
            return True
        if x is None or y is None:
            return False
        return x.val==y.val and self.equals(x.left,y.left) and self.equals(x.right,y.right)

#Time complexity : O(m*n). In worst case(skewed tree) traverse function takes O(m*n) time.

#Space complexity : O(n). The depth of the recursion tree can go upto n. n refers to the number of nodes in s.

'''
In O(n) time complexity

// in-order traversal in array format
function in_order(root, nodes) {
    if (root && root.left) {
        in_order(root.left, nodes);
    }
    nodes.push(root.data);
    if (root && root.right) {
        in_order(root.right, nodes);
    }
    return nodes;
}

// pre-order traversal in array format
function pre_order(root, nodes) {
    nodes.push(root.data);
    if (root && root.left) {
        pre_order(root.left, nodes);
    }
    if (root && root.right) {
        pre_order(root.right, nodes);
    }
    return nodes;
}

// function that takes two root nodes and determines if
// the first tree is a subtree of the second tree
function is_subtree(root, root_r) {

    // the variables below will hold the values:
    // 4-30-10-6
    // 4-30-10-6-26-3-3
    var inord1 = in_order(root, []).join('-');
    var inord2 = in_order(root_r, []).join('-');

    // 10-4-30-6
    // 26-10-4-30-6-3-3
    var preord1 = pre_order(root, []).join('-');
    var preord2 = pre_order(root_r, []).join('-');

    // check if the left tree is contained with the right tree
    return inord2.indexOf(inord1) !== -1 && preord2.indexOf(preord1) !== -1;

}

is_subtree(root, root_r); // => true
'''
