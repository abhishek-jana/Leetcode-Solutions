'''
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.
Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.


Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

'''
'''
A A A n =2
A I I A I I A
output = 7
A A A B B n=2
A B I A B I A
output = 7
idle = (max_occuring_number - 1)*n
counter =number of max_occuring_number
intervals = (max_accouring_number-1)*(n+1) + counter
max (len(tasks), intervals)
'''
'''

Time complexity for this solution will be O(n). We first iterate through the entire list to keep counts (O(n)). Then, we sort based on the values which typically comes out to O(nlogn) BUT we know that we are only ever sorting 26 letters maximum, so we only need 26 elements to sort and so our n = 26. This makes sorting a constant time operation = 26log26 = constant number not dependent on n therefore O(1). After, we iterate again to count how many max values we have that are also our maximum, and this again should be order O(n), but we are only iterating over 26 elements, so we know our while loop will terminate after 26 elements since len(lst) is bounded by 26. And finally, we do constant time calculations, so our overall time complexity is just O(n).

Our space complexity is also O(1) since we only need a dictionary with 26 keys.
** We will never have more than 26 letters so the keys in our dictionary are bound by 26 and therefore so is the length of the lst we maintain.
'''
class Solution:
    def leastInterval(self, tasks, n):
        d = {}
        for i in tasks:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        lst = sorted(d.values(),reverse=True)
        max_number = lst[0]
        i = 0
        counter = 0
        while i < len(lst) and lst[i] == max_number:
            counter += 1
            i += 1
        return max((max_number-1)*(n+1) + counter,len(tasks))
