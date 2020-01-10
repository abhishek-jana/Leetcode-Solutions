'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
'''
'''
# idea is based on level order traversal using two queues
"""
Python program to do level order traversal
line by line using dual queue"""
class GFG:

    """Constructor to create a new tree node"""
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None

    """Prints level order traversal line by
    line using two queues."""
    def levelOrder(self,node):
        q1 = [] # Queue 1
        q2 = [] # Queue 2
        q1.append(node)

        """Executing loop till both the
        queues become empty"""
        while(len(q1) > 0 or len(q2) > 0):

            """Empty string to concatenate
            the string for q1"""
            concat_str_q1 = ''
            while(len(q1) > 0):

                """Poped node at the first
                pos in queue 1 i.e q1"""
                poped_node = q1.pop(0)
                concat_str_q1 += poped_node.val +' '

                """Pushing left child of current
                node in first queue into second queue"""
                if poped_node.left:
                    q2.append(poped_node.left)

                """Pushing right child of current node
                in first queue into second queue"""
                if poped_node.right:
                    q2.append(poped_node.right)
            print( str(concat_str_q1))
            concat_str_q1 = ''

            """Empty string to concatenate the
            string for q1"""
            concat_str_q2 = ''
            while (len(q2) > 0):

                """Poped node at the first pos
                in queue 1 i.e q1"""
                poped_node = q2.pop(0)
                concat_str_q2 += poped_node.val + ' '

                """Pushing left child of current node
                in first queue into first queue"""
                if poped_node.left:
                    q1.append(poped_node.left)

                """Pushing right child of current node
                in first queue into first queue"""
                if poped_node.right:
                    q1.append(poped_node.right)
            print(str(concat_str_q2))
            concat_str_q2 = ''

""" Driver program to test above functions"""
node = GFG("1")
node.left = GFG("2")
node.right = GFG("3")
node.left.left = GFG("4")
node.left.right = GFG("5")
node.right.right = GFG("6")
node.levelOrder(node)
'''
'''
# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
        pass

    def bfs(self,root):
        arr = []
        if root.left is None and root.right is None:
            return
        left = root.left
        right = root.right
        #avg = (left+right)/2
        return (self.bfs(root.left) + self.bfs(root.right))/2

def printLevelOrder(root):
    h = height(root)
    for i in range(1,h+1):
        printGivenLevel(root,i)

def printGivenLeve(root,level):
    if root is None:
        return 0
    if level == 1:
        return root.val, level
    elif level>1:
        printGivenLevel(root.left,level-1)
        printGivenLevel(root.right,level-1)

def height(node):
    if node in None:
        return 0

    lheight = height(node.left)
    rheight = height(node.right)
    if lheight > rheight:
        return lheight+1
    else:
        return rheight+1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Level order traversal of binary tree is -")
printLevelOrder(root)
'''
'''
# Recursive Python program for level order traversal of Binary Tree

# A node structure
class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)


# Print nodes at a given level
def printGivenLevel(root , level):
    if root is None:
        return
    if level == 1:
        print ("%d" %(root.data)),
    elif level > 1 :
        printGivenLevel(root.left , level-1)
        printGivenLevel(root.right , level-1)


""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""
def height(node):
    if node is None:
        return 0
    else :
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        #Use the larger one
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Level order traversal of binary tree is -")
printLevelOrder(root)
'''
# Best Explanation

#http://yueguo1217.com/leetcode-637-average-of-levels-in-binary-tree-easy-75-in-python/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res=[]
        if not root: return res
        q=[root]
        while q:
            q1=[]
            total=0
            cnt=0
            while q:
                node =q.pop()
                if node.left: q1.append(node.left)
                if node.right: q1.append(node.right)
                total+=node.val
                cnt+=1
            res.append(total*1.0/cnt)
            q=list(q1)
        return res
