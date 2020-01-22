'''
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
'''
'''
A classic greedy case: interval scheduling problem.

The heuristic is: always pick the interval with the earliest end time. Then you can get the maximal 
number of non-overlapping intervals. (or minimal number to remove).
This is because, the interval with the earliest end time produces the maximal capacity to hold rest intervals.
E.g. Suppose current earliest end time of the rest intervals is x. 
Then available time slot left for other intervals is [x:]. If we choose another interval with end time y, 
then available time slot would be [y:]. Since x ≤ y, there is no way [y:] can hold more intervals then [x:].
Thus, the heuristic holds.

Therefore, we can sort interval by ending time and key track of current earliest end time. 
Once next interval's start time is earlier than current end time, then we have to remove one interval. 
Otherwise, we update earliest end time.
'''
def eraseOverlapIntervals(intervals):
	end, cnt = float('-inf'), 0
	for i in sorted(intervals, key=lambda x: x[1]):
		if i[0] >= end:
			end = i[1]
		else:
			cnt += 1
	return cnt
#Time complexity is O(NlogN) as sort overwhelms greedy search.

# Faster
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # O(nlogn) for the sort


        return_counter = 0

        last_index = 0

        intervals.sort(key=lambda x: x[1])

        for i in range(1, len(intervals)):
            if intervals[last_index][1] > intervals[i][0]:
                return_counter += 1
            else:
                last_index = i

        return return_counter
