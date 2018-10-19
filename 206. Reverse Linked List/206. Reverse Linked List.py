# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        else:
            G = head
            T = head.next
            head.next = None
            while T !=  None:
                S = T.next
                T.next = G
                G = T
                T = S
            return G
