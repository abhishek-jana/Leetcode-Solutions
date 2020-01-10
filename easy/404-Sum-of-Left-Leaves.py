'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''
# Iterative solution
# Python program to find sum of all left leaves

# A binary tree node


class Node:

    # A constructor to create a new Node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Return the sum of left leaf nodes
def sumOfLeftLeaves(root):
    if(root is None):
        return 0

    # Using a stack for Depth-First Traversal of the tree
    stack = []
    stack.append(root)

    # sum holds the sum of all the left leaves
    sum = 0

    while len(stack) > 0:
        currentNode = stack.pop()

        if currentNode.left is not None:
            stack.append(currentNode.left)

            # Check if currentNode's left child is a leaf node
            if currentNode.left.left is None and currentNode.left.right is None:

                # if currentNode is a leaf, add its data to the sum
                sum = sum + currentNode.left.data

        if currentNode.right is not None:
            stack.append(currentNode.right)
    return sum


# Driver Code
root = Tree(20)
root.left = Tree(9)
root.right = Tree(49)
root.right.left = Tree(23)
root.right.right = Tree(52)
root.right.right.left = Tree(50)
root.left.left = Tree(5)
root.left.right = Tree(12)
root.left.right.right = Tree(12)

print('Sum of left leaves is {}'.format(sumOfLeftLeaves(root)))

# recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:
                if is_left:
                    return node.val
                return 0
            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)
