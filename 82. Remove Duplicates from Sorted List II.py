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
        hash table: store the val which has appeared.
        """
        if head == None: # head = []
            return head
        if head.next == None: # head = [n1]
            return head
        
        A = set() # save the duplicated numbers
        p = head
        while p.next != None:
            if p.val == p.next.val:
                A.add(p.val)
            p = p.next
            
        prevp = head # remove duplicate from the front
        while prevp != None and prevp.val in A:
                prevp = prevp.next
        head = prevp
        
        if prevp == None:
            return head
        
        currp = prevp.next
        while currp != None:
            if currp.val in A:
                currp = currp.next
            else:
                prevp.next = currp
                prevp = currp
                currp = currp.next
        prevp.next = None
        return head            
