# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return []
            
        if head.next == None:
            return head
            
        A = [ListNode(0) for i in range(k+1)]
        if k == 1:
            return head
            
        for i in range(k+1):
            A[i] = head
        j = 1
        while i >= 1:
            if A[k] == None:
                print ("Ggg", j)
                return head
            for m in range(j):
                A[k-m] = A[k-m].next
            j = j + 1
            i = i - 1
        A[0].next = A[k]
        for i in range(1, k):
            A[i].next = A[i-1]
        head = A[k-1]
        if A[k] == None:
            return head
        while True:
            D = A[0]
            D.next = None
            for i in range(0, k):
                A[i] = A[k]
            j = 1
            G = A[k]
            while i >= 0:
                if A[k] == None:
                    D.next = G
                    print("jjj|_|")
                    return head
                for m in range(j):
                    A[k-m] = A[k-m].next
                j = j + 1
                i = i - 1

            for i in range(1, k):
                A[i].next = A[i-1]
                print A[i].val
            A[0].next = A[k]
            D.next = A[k-1]
    
