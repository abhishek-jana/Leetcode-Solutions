# https://leetcode.com/problems/word-search/
"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
def exist(self, board, word):
    if not word:
        return True
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if self.exist_helper(board, word, i, j):
                return True
    return False

def exist_helper(self, board, word, i, j):
    if board[i][j] == word[0]:
        if not word[1:]:
            return True
        board[i][j] = " " # indicate used cell
        # check all adjacent cells
        if i > 0 and self.exist_helper(board, word[1:], i-1, j):
            return True
        if i < len(board)-1 and self.exist_helper(board, word[1:], i+1, j):
            return True
        if j > 0 and self.exist_helper(board, word[1:], i, j-1):
            return True
        if j < len(board[0])-1 and self.exist_helper(board, word[1:], i, j+1):
            return True
        board[i][j] = word[0] # update the cell to its original value
        return False
    else:
        return False

# Faster
from collections import Counter
class Solution:
    def exist(self, board, word):
        """72ms! Beats 98.21% of submissions as of 23 March, 2019.
        Time Complexity: Still O(mn*4^k) where board is m*n in size, and word length = k.
        Uses a pre-check to skip execution for boards without the required characters.
        Uses a DFS otherwise, with 4 branches, and a depth of k, the length of the word.
        """
        def pre_check():
            """Checks whether board has all the characters required in word
            """
            chars_required = Counter(word)

            # Mark down the characters required, if they appear in the board
            for row in board:
                for char in row:
                    if char in chars_required and chars_required[char] > 0:
                        chars_required[char] -= 1

            # Ensure the board has all of the characters required for the word
            for count in chars_required.values():
                if count > 0:
                    return False
            return True

        def path_exists(char_ind, x, y):
            """DFS checking for path existence.
            """
            # Reject case
            if board[x][y] != word[char_ind]:
                return False

            # Base case
            elif char_ind == l - 1:
                return True

            # Recursive Case
            char_ind += 1

            # Temporarily mark the board position with None
            board[x][y] = None

            # Check each possible direction
            for d in [(0, 1),(0, -1),(1, 0),(-1, 0)]:
                next_x, next_y = x + d[0], y + d[1]
                # Only explore the move if it's valid and hasn't already been explored
                if -1 < next_x < m and -1 < next_y < n and board[next_x][next_y]:
                    if path_exists(char_ind, next_x, next_y):
                        return True

            # Change the board back to its original character
            board[x][y] = word[char_ind - 1]
            return False

        # Initial Checks
        if not board:
            return False
        if not word:
            return True
        if not pre_check():
            return False

        # Check paths starting from each character in the board
        m, n, l = len(board), len(board[0]), len(word)
        for i in range(m):
            for j in range(n):
                if path_exists(0, i, j):
                    return True

        # False if no such path exists.
        return False
