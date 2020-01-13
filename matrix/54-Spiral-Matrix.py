"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if len(matrix) == 0:
            return []

        if len(matrix) == 1:
            return matrix[0]

        R = len(matrix)
        C = len(matrix[0])

        x1, y1 = 0, 0
        x2, y2 = 0, C-1
        x3, y3 = R-1, C-1
        x4, y4 = R-1, 0

        res = []

        while len(res) < R*C:

            visited = []
            visited.extend(matrix[x1][y1:y2+1])
            visited.extend([matrix[x][y2] for x in range(x2,x3+1)])
            visited.extend(matrix[x3][::-1])
            visited.extend([matrix[x][y4] for x in range(x4, x1-1, -1)])

            [res.append(x) for x in visited if x not in res]

            x1, y1 = x1+1, y1+1
            x2, y2 = x2+1, y2-1
            x3, y3 = x3-1, y3-1
            x4, y4 = x4-1, y4+1

        return res

class Solution:

    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
