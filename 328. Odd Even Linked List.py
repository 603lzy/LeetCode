# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        elif head.next == None:
            return head
        elif head.next.next == None:
            return head
        po = head
        pe = head.next
        # more than 2 nodes
        ohead = head.next
        while pe.next != None and pe.next.next != None:
            po.next = pe.next
            po = po.next
            pe.next = po.next
            pe = pe.next
        if pe.next == None:
            po.next = ohead
        else:
            po.next = pe.next
            po.next.next = ohead
            pe.next = None
        return head
