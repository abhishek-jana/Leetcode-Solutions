'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
"""
Similar problems
252 Meeting Rooms
253 Meeting Rooms II
435 Non-overlapping Intervals
"""

# Time O(nlogn)
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0: return []
        intervals = sorted(intervals, key = lambda x: x[0])
        res = [intervals[0]]
        for n in intervals[1:]:
            if n[0] <= res[-1][-1]: res[-1][-1] = max(n[-1], res[-1][-1])
            else: res.append(n)
        return res
'''
intervals [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals.sort [[1, 3], [2, 6], [8, 10], [15, 18]]

interval = [1,3]
merged =[]
not merged:
	merged =[ [1,3] ]

interval =[2,6]
merged = [ [1,3] ]
merged[-1][-1] = 3 > interval[0] = 2:
	merged[-1][-1] = max(merged[-1][-1] = 3 ,interval[-1] = 6) =6
merged = [[1,6]]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =lambda x: x[0])
        merged =[]
        for i in intervals:
			# if the list of merged intervals is empty
			# or if the current interval does not overlap with the previous,
			# simply append it.
            if not merged or merged[-1][-1] < i[0]:
                merged.append(i)
			# otherwise, there is overlap,a
			#so we merge the current and previous intervals.
            else:
                merged[-1][-1] = max(merged[-1][-1], i[-1])
        return merged
Time complexity:
In python, use sort method to a list costs O(nlogn), where n is the length of the list.
The for-loop used to merge intervals, costs O(n).
O(nlogn)+O(n) = O(nlogn)
So the total time complexity is O(nlogn).
Space complexity
The algorithm used a merged list and a variable i.
In the worst case, the merged list is equal to the length of the input intervals list. So the space complexity is O(n), where n is the length of the input list.
'''
