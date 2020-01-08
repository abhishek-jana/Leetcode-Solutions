'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = ListNode(new_data)  # creates a node
        # changes the next reference of new node to refer to the old first node of the list
        new_node.next = self.head
        self.head = new_node  # Move the head to point to new Node

    def isPalindrome(self):
        #p = self.head
        #s = ""
        #p = head
        #while p:
        #    s = s.append(p.val)
        #    p = p.next
        #return s == s[::-1]
        # Method 2
        #p = self.head
        #s = []
        #while p:
        #    s.append(p.val)
        #    p = p.next
        #p = self.head
        #while p:
        #    data = s.pop()
        #    if p.val != data:
        #        return False
        #    p = p.next
        #return True
        # Method 3
        p = self.head
        q = self.head
        prev = []

        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i-1]

        count = 0

        while count <= i//2 :
            if prev[-(count+1)].val != p.val:
                return False
            p = p.next
            count += 1
        return True
    def printlist(self):
        while self.head:
            print (self.head.val)
            self.head = self.head.next

llist = Linkedlist()
llist.push("R")
llist.push("A")
llist.push("C")
llist.push("E")
llist.push("C")
llist.push("A")
llist.push("R")
llist_2 = Linkedlist()
llist_2.push("A")
llist_2.push("B")
llist_2.push("C")
print(llist_2.isPalindrome())
#print (llist.printlist())
print (llist.isPalindrome())

# more efficient than s = s[::-1]
def check_palin(word):
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            return False
    return True
print (check_palin('ABBBA'))
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 #Source: http://yucoding.blogspot.com/2016/01/leetcode-question-palindrome-linked-list.html
class Solution(object):

    def reverse(self, head):
        p = head.next
        while p and p.next:
            tmp = p.next
            p.next = p.next.next
            tmp.next = head.next
            head.next = tmp

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        #get middle pointer
        p1 = ListNode(0)
        p1.next = head
        p2 = p1
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        # reverse second half of list
        self.reverse(p1)

        # check palindrome
        p1 = p1.next
        p2 = head
        while p1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
