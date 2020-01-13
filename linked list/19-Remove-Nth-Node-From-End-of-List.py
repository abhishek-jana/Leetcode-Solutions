# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
"""
So the trick here i used was,
First i went to the terminal or terminating Node Node using the DFS or Recursion then at the time i was returning i passed a number 1 and increment it on each step which was the count of the node from the last thus when i was at the node 1 greater than the actual node to be removed i simply ditched that node and wala its done

But there was one case when the starting node will be removed for that i used common sense ,if there was any ditching in bettwen the returns of the recursion then i will return None or else i will return the Numbers , in short if i have already ditched a node then i will return the counter as None or else i will keep counting and in that case in the main body of the code when i get the result of the recursion then i check if the result is None then the swaping is already done but if i get a Number that means no swaping is done and its the first Node which needs to be ditched then i simply ditched first Node and get My result , so here is the simple code to visulaize what is happening here .
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getNthLast(node, count, pos):
            if node != None:
                res = getNthLast(node.next, count + 1, pos)
                if res == None:
                    return None
                if res != pos + 1 :
                    return res +1
                else:
                    node.next = node.next.next
                    return None
            else:
                return 1
        count = getNthLast(head, 0, n)
        if count != None:
            return head.next
        return head
