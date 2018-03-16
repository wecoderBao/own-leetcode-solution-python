"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 添加一个头指针
        dummy = ListNode(-1)
        dummy.next = head
        start = dummy
        target = dummy
        while start.next is not None:
            n -= 1
            start = start.next
            if n < 0:
                target = target.next
        target.next = target.next.next
        return dummy.next