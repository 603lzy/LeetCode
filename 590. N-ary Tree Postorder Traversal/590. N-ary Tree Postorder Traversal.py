"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack1, stack2 = [root], []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            stack1 += node.children
        return [node.val for node in stack2[::-1]]
            
