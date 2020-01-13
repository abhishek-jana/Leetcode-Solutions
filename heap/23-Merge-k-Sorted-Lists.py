# https://leetcode.com/problems/merge-k-sorted-lists/
'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
# If n is the length of the list, k is the average length of link, then the heap operations should take O(log(n)). The final complexity will be O(nklog(n))
class Solution:
    def mergeKLists(self, lists):
        from heapq import heappush, heappop, heapreplace, heapify
        dummy = node = ListNode(0)
        ## If two elements have the same val, the next tuple items will be compared:
## "i" in the below code, which is guaranteed to be unique.
        heap = [(head.val, i, head) for i,head in enumerate(lists) if head]
        heapify(heap)
        dummy = ListNode(0)
        curr = dummy
        while heap != []:
            val, i, node = heap[0]
            if not node.next: # exhausted one linked-list
                heappop(heap)
            else:
                heapreplace(heap, (node.next.val, i, node.next)) # recycling tie-breaker i guarantees uniqueness
            curr.next = node
            curr = curr.next
        return dummy.next
# DC python solution O(nk log k) runtime, O(1) space
def mergeKLists(self, lists):
    if not lists:
        return None
    start = 0
    end = len(lists) - 1
    while start != end or end != 0:
        if start >= end:
            start = 0
        else:
            lists[start] = self.mergeTwoLists(lists[start], lists[end])
            start += 1
            end -= 1
    return lists[0]

def mergeTwoLists(self, l1, l2):
    current = head = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return head.next
