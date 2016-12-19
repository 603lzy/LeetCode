# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        p = head
        A = [] # save all the vals in list
        while p != None:
            A.append(p.val)
            p = p.next
        p = head
        for i in A:
            if i < x:
                p.val = i
                p = p.next # get smaller value
        for i in A:
            if i >= x:
                p.val = i
                p = p.next # get bigger value
        return head
