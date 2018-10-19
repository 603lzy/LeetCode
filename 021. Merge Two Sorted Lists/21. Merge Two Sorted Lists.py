# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2 # use two pointers point to locate pos in two lists
        if p1 == None:
            return l2
        elif p2 == None:
            return l1
        elif p1.val <= p2.val:
            head = p1     # first node is same with l1 if its value smaller
            p1 = p1.next
        else:
            head = p2
            p2 = p2.next
        p = head # pointer p point to the current node
        while (p1 != None or p2 != None):
            if p1 == None: # if l1 ends
                p.next = p2
                p2 = p2.next
            elif p2 == None:
                p.next = p1
                p1 = p1.next
            elif p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else: # if p2.val < p1.val
                p.next = p2
                p2 = p2.next
            p = p.next
        return head
