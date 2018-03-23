"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
 If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 注意特殊情况， k == 1时的情况
        if k == 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        q = dummy
        flag = False
        count = 0
        while p.next:
            p = p.next
            if flag:
                q = q.next
            count += 1
            if count == k:
                temp = q.next
                tempHead = q.next
                while temp != p:
                    node = temp
                    temp = temp.next
                    node.next = q.next
                    q.next = node
                tempHead.next = p.next
                p.next = q.next
                q.next = p
                p = tempHead
                count = 0
                flag = True
        return dummy.next


