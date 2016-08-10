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
        lenh = 0
        l1 = head
        if head == None:
            return None
        elif head.next ==  None:
            return head
        else:
            D = head
            G = head
            S = head.next
            T = head.next.next
            G.next = T
            S.next = G
            D = S
            head = D
            while(G != None) and (S != None) and (T != None):
                if S.next.next.next == None:
                    break
                else:
                    T = T.next.next
                    S = S.next.next.next
                    G = G.next
                    D = D.next
                    D.next = None
                    G.next = T
                    S.next = G
                    D.next = S
                    D = D.next
            return head
                    
        
            
            
