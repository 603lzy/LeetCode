# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        else:
            C = head # the current node
            T = head.next # the next node
            G = None
            head.next = G
            while T != None:
                if T.val == C.val:
                    T = T.next
                else:
                    G = T
                    T = T.next
                    C.next = G
                    C = G
                    G = None
                    C.next = G
            return head
        
