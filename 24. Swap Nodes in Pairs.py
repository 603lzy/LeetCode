# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        D, G, S, T = head, head, head.next, head.next.next
        G.next = T
        S.next = G
        D = S
        head = D
        while(G != None) and (S != None) and (T != None):
            if S.next.next.next:
                T, S, G, D = T.next.next, S.next.next.next, G.next, D.next
                D.next = None
                G.next = T
                S.next = G
                D.next = S
                D = D.next
            else:
                break
        return head
