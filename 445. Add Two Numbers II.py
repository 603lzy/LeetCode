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
        n1, n2 = 0, 0 # save two numbers
        p1, p2 = l1, l2 # point to the head of two list
        while (p1 != None):
            n1 = n1 * 10 + p1.val
            p1 = p1.next
        while (p2 != None):
            n2 = n2 * 10 + p2.val
            p2 = p2.next
        strn = str(n1 + n2)
        head = curNode = ListNode(int(strn[0]))
        for i in xrange(1, len(strn)):
            curNode.next = ListNode(int(strn[i])) # current node point to a new node, which val is a number
            curNode = curNode.next
        return head
