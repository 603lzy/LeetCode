# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fp = sp = head
        for i in xrange(n):
            fp = fp.next
        if not fp:
            return head.next
        while fp.next:
            fp, sp = fp.next, sp.next
        sp.next = sp.next.next
        return head
