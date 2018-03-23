"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
 You may not modify the values in the list, only nodes itself can be changed
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        q = dummy
        count = 0
        flag = False
        while p.next:
            p = p.next
            if flag:
                q = q.next
            count += 1
            if count == 2:
                q.next.next = p.next
                p.next = q.next
                q.next = p
                p = q.next.next
                count = 0
                flag = True
        return dummy.next

