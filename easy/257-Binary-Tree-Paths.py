'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Time:  O(n * h)
# Space: O(h)


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        paths = []

        curr = ""
        self.dfs(root, curr, paths)
        return paths

    def dfs(self, root, curr, paths):
        if root.left is None and root.right is None:
            paths.append(curr + str(root.val))
            return paths

        if root.left:
            self.dfs(root.left, curr + str(root.val) + '->', paths)
        if root.right:
            self.dfs(root.right, curr + str(root.val) + '->', paths)

# Time:  O(n * h)
# Space: O(h)


class Solution(object):
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result, path = [], []
        self.binaryTreePathsRecu(root, path, result)
        return result

    def binaryTreePathsRecu(self, node, path, result):
        if node is None:
            return

        if node.left is node.right is None:
            ans = ""
            for n in path:
                ans.append(str(n.val) + "->")
            result.append(ans + str(node.val))

        if node.left:
            path.append(node)
            self.binaryTreePathsRecu(node.left, path, result)
            path.pop()

        if node.right:
            path.append(node)
            self.binaryTreePathsRecu(node.right, path, result)
            path.pop()
