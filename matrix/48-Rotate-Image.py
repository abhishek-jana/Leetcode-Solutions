# https://leetcode.com/problems/rotate-image/
"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
# https://leetcode.com/problems/rotate-image/discuss/367514/python-beats-96-with-Image-helps-u-understand
class Solution(object):
    def rotate(self, matrix: List[List[int]]) -> None:
        def rotate_pos_clockwise(i,j):
            return j,self.n-1-i

        n = len(matrix)
        self.n = n
        if(n<=1): return
        for i in range((n+1)//2):
            for j in range(i,n-i-1):
                up_val = matrix[i][j]
                i_right,j_right = rotate_pos_clockwise(i,j)
                i_bottom,j_bottom = rotate_pos_clockwise(i_right,j_right)
                i_left,j_left = rotate_pos_clockwise(i_bottom,j_bottom)
                matrix[i][j] = matrix[i_left][j_left]
                matrix[i_left][j_left] = matrix[i_bottom][j_bottom]
                matrix[i_bottom][j_bottom] = matrix[i_right][j_right]
                matrix[i_right][j_right] = up_val
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        # transpose
        for i in range(n):
            for j in range(i + 1, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        # flip horizontally
        for i in range(n):
            for j in range(n/2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n - 1 - j]
                matrix[i][n - 1- j] = tmp

# https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)
