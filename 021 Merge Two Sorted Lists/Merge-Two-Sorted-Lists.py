"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode(-1)
        p = head
        while l1 and l2:
            if l1.val > l2.val:
                p.next = l2
                l2 = l2.next
            elif l1.val == l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
                p.next = l2
                l2 = l2.next
            else:
                p.next = l1
                l1 = l1.next
            p = p.next

        ll = l1 or l2
        p.next = ll
        return head.next