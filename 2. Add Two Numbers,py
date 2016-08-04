# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        M = []
        N = []
        T = ListNode(0)
        while l1 != None:
            M.append(l1.val)
            l1 = l1.next
        m = 0
        for i in range(0, len(M)):
            m = (10 ** i) * M[i] + m
        while l2 != None:
            N.append(l2.val)
            l2 = l2.next
        n = 0
        for i in range(0, len(N)):
            n = (10 ** i) * N[i] + n
        s = n + m
        i = len(str(s))
        while i > 0:
            i = i - 1
            T.val = s//(10**i)
            print(T.val, i)
            S = ListNode(0)
            S.next = T
            T = S
            s = s%(10**i)
        
        S = S.next 
        return S
