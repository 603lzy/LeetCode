# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# ref:
# https://docs.python.org/3/glossary.html#term-eafp Easier to ask for forgiveness than permission
# Wonderful!! Cycle detection Turtoise and hare
# https://discuss.leetcode.com/topic/16098/except-ionally-fast-python/10

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
        
