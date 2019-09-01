'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur_l1 = l1
        cur_l2 = l2
        head = ListNode(None)
        cur_p = head
        while cur_l1 and cur_l2:
                if cur_l1.val < cur_l2.val:
                        cur_p.next = cur_l1
                        cur_l1 = cur_l1.next
                        cur_p = cur_p.next
                else:
                        cur_p.next = cur_l2
                        cur_l2 = cur_l2.next
                        cur_p = cur_p.next
        cur_p.next = cur_l1 or cur_l2
        return head.next

x1 = ListNode(1)
x2 = ListNode(2)
x3 = ListNode(4)
x1.next = x2
x2.next = x3

y1 = ListNode(1)
y2 = ListNode(3)
y3 = ListNode(4)
y1.next = y2
y2.next = y3

Solution().mergeTwoLists(x1,y1)