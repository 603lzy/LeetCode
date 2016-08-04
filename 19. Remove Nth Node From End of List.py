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
        lenl = 1
        tmp0 = head
        while tmp0 != None:
            print tmp0.val, lenl
            tmp0 = tmp0.next
            lenl = lenl + 1
        
        print("================")
        i = 1
        tmp1 = head
        while (lenl - n) - i > 0:
            print i, tmp1.val
            i = i + 1
            tmp1 = tmp1.next
        print tmp1.val
        print("================")
