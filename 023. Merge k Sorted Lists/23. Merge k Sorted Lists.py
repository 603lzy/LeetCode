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
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            D = []
            while (l1 != None) and (l2 != None):
                if l1.val <= l2.val:
                    D.append(l1.val)
                    l1 = l1.next
                else:
                    D.append(l2.val)
                    l2 = l2.next
            while l1 != None:
                D.append(l1.val)
                l1 = l1.next
            while l2 != None:
                D.append(l2.val)
                l2 = l2.next
            lend = len(D)
            i = lend  - 1
            S = ListNode(D[i])
            i = i - 1
            while i >= 0:
                T = ListNode(D[i])
                T.next = S
                S = T
                i = i - 1
            return S
            
            
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return lists
        if len(lists) == 1:
            return lists[0]
        while len(lists) >= 2:
            S = self.mergeTwoLists(lists[-1], lists[-2])
            lists.pop()
            lists.pop()
            lists.append(S)
        return lists[0]

            
