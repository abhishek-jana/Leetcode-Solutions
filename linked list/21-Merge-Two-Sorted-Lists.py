# https://leetcode.com/problems/merge-two-sorted-lists/
'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
'''
Solution 1

If both lists are non-empty, I first make sure a starts smaller, use its head as result, and merge the remainders behind it. Otherwise, i.e., if one or both are empty, I just return what's there.
'''
class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b
'''
Solution 2

First make sure that a is the "better" one (meaning b is None or has larger/equal value). Then merge the remainders behind a.
'''
# Best
def mergeTwoLists(self, a, b):
    if not a or b and a.val > b.val:
        a, b = b, a
    if a:
        a.next = self.mergeTwoLists(a.next, b)
    return a
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = sort_list = ListNode(0)

        while(l1 and l2):
            if (l1.val < l2.val):
                sort_list.next = l1
                l1 = l1.next
                sort_list = sort_list.next

            elif (l1.val >= l2.val):
                sort_list.next = l2
                l2 = l2.next
                sort_list = sort_list.next

        sort_list.next = l1 or l2
        return head.next
