"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        maxDepth()
        1. If tree is empty then return 0
        2. Else
            (a) Get the max depth of each child of the current root recursively
            (b) Get the max of max depths from (a)
            (c) Return max_depth = max(b) + 1
        Note that:
        add"[0]" in max() in case the error raised because there is no children for current node.
        """
        if root is None:
            return 0
        else:
            childrenDepth = []
            for childnode in  root.children:
                childrenDepth.append(self.maxDepth(childnode))
            return max([0] + childrenDepth) + 1 
            
