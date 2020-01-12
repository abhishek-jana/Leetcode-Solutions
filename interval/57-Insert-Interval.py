"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    # @should rewrite without sort!!!
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x.start)
        length=len(intervals)
        res=[]
        for i in range(length):
            if res==[]:
                res.append(intervals[i])
            else:
                size=len(res)
                if res[size-1].start<=intervals[i].start<=res[size-1].end:
                    res[size-1].end=max(intervals[i].end, res[size-1].end)
                else:
                    res.append(intervals[i])
        return res

# O(nlgn) time, the same as Merge Intervals
# https://leetcode.com/problems/merge-intervals/
def insert1(self, intervals, newInterval):
    intervals.append(newInterval)
    res = []
    for i in sorted(intervals, key=lambda x:x.start):
        if res and res[-1].end >= i.start:
            res[-1].end = max(res[-1].end, i.end)
        else:
            res.append(i)
    return res

# O(n) time, not in-place, make use of the
# property that the intervals were initially sorted
# according to their start times
def insert(self, intervals, newInterval):
    res, n = [], newInterval
    for index, i in enumerate(intervals):
        if i.end < n.start:
            res.append(i)
        elif n.end < i.start:
            res.append(n)
            return res+intervals[index:]  # can return earlier
        else:  # overlap case
            n.start = min(n.start, i.start)
            n.end = max(n.end, i.end)
    res.append(n)
    return res
