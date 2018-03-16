"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoList(l1, l2):
            head = ListNode(-1)
            p = head
            while l1 and l2:
                if l1.val > l2.val:
                    p.next = l2
                    l2 = l2.next
                else:
                    p.next = l1
                    l1 = l1.next
                p = p.next
            return head.next
        def mergeAll(lists, left, right):
            if left == right:
                return lists[left]
            if left < right:
                mid = (left + right) // 2
                leftlist = mergeAll(lists, left, mid)
                rightlist = mergeAll(lists, mid+1, right)
                return mergeTwoList(leftlist, rightlist)
        return mergeAll(lists, 0, len(lists-1))

