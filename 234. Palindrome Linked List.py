# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        A = []
        while head != None:
            A.append(head.val)
            head = head.next
        if A == A[::-1]:
            return True
        else:
            return False
