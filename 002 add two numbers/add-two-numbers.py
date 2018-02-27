"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        resultNode = ListNode(0)
        temp = resultNode
        more = 0
        previous = None
        while l1 and l2:
            temp.val = l1.val + l2.val + more
            more = temp.val // 10
            temp.val = temp.val % 10
            l1 = l1.next
            l2 = l2.next
            temp.next = ListNode(0)
            previous = temp
            temp = temp.next

        res = l1 or l2
        while res:
            temp.val = res.val + more
            more = temp.val // 10
            temp.val = temp.val % 10
            res = res.next
            temp.next = ListNode(0)
            previous = temp
            temp = temp.next

        if more > 0:
            temp.val = more
            temp.next = None
        else:
            previous.next = None

        return resultNode


n1 = ListNode(1)
n2 = ListNode(8)
n1.next = n2
l1 = n1
n1 = ListNode(0)
l2 = n1

addtwo = Solution()
l3 = addtwo.addTwoNumbers_2(l1, l2)
while l3:
    print(l3.val)
    l3 = l3.next

