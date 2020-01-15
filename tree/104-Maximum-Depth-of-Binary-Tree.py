"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# BFS
class Solution(object):
    def maxDepth(self, root):
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue
        return depth

# DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        stack = [(root, 1)]
        while stack:
            root, leng = stack.pop()
            if not root:
                return 0
            if leng > depth:
                depth = leng
            if root.right:
                stack.append((root.right, leng + 1))
            if root.left:
                stack.append((root.left, leng + 1))
        return depth
