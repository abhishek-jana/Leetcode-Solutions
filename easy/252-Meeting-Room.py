'''
Given an array of meeting time intervals consisting of start and end times [s1, e1], [s2, e2], ... , determine if a person could attend all meetings.

For example,
Given [ [0, 30], [5, 10], [15, 20] ],
return false
'''


class Interval(object):
        def __init__(self, s=0, e=0):
            self.start = s
            self.end = e
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        length = len(intervals)
        intervals.sort(key = lambda x : x.start)
        for i in range(length-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True

# Time:  O(nlogn) because of sorting.
# Space: O(n)

print (interval.sort(key=lambda x:x.start))
