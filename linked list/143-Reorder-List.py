# https://leetcode.com/problems/reorder-list/
"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
"""
For linked list 1->2->3->4-5, the code first makes the list to be 1->2->3->4<-5 and 4->None, then make 3->None, for even number linked list: 1->2->3->4, make first 1->2->3<-4 and 3->None, and lastly do not forget to make 2->None.
"""
def reorderList(self, head):
    if not head:
        return
    # ensure the first part has the same or one more node
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the second half
    p = slow.next
    slow.next = None
    node = None
    while p:
        nxt = p.next
        p.next = node
        node = p
        p = nxt
    # combine head part and node part
    p = head
    while node:
        tmp = node.next
        node.next = p.next
        p.next = node
        p = p.next.next #p = node.next
        node = tmp
class Solution(object):
    def reorderList(self, head):
        if not head: return
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        pre, slow.next, slow = None, None, slow.next
        while slow:
            slow.next, pre, slow = pre, slow, slow.next
        while head and pre:
            head.next, head, pre.next, pre = pre, head.next, head.next, pre.next
