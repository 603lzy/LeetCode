# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        else:
            A = []
            p = head
            while p != None:
                A.append(p.val)
                p = p.next
            p = head
            cnt = 1
            while cnt < m:
                p.val = A[cnt - 1]
                p = p.next
                cnt += 1
            for i in xrange(n, m-1, -1):
                p.val = A[i-1]
                p = p.next
                cnt += 1
            while n < cnt <= len(A):
                p.val = A[cnt - 1]
                p = p.next
                cnt += 1
            return head
