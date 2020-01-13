# https://leetcode.com/problems/linked-list-cycle/
"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.




Follow up:

Can you solve it using O(1) (i.e. constant) memory?
"""

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if head == None or head.next == None :
            return False

        prev = head
        current = head.next

        while current.next != None :

#Using the 2 pointers, current moves 2 step while prev move 1 step
#So that if it's a circle current will be able to chase and meet with prev

            current = current.next.next
            prev = prev.next

#If current and prev met in the chase return True

            if current == prev :
                return True

#When it reached at the end of LinkedList element
#and next is None return False

            if current == None or current.next == None :
                return False

        return False

# https://www.youtube.com/watch?time_continue=363&v=0DqxhTiVPGM&feature=emb_logo
